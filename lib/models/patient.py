# lib/models/patient.py
from lib.cli import CONN, CURSOR

class Patient:
    all = {}
    def __init__(self, name, last_name, age ,symptoms=None, id=None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.symptoms = symptoms or []

    def __repr__(self):
        return (
        f'<Patient {self.id}: {self.name}, {self.last_name}, {self.age}, ' + 
            f'Symptom: {self.symptoms}>'
        )
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
       if isinstance(name, str) and len(name):
           self._name = name
       else:
           raise ValueError('Name must be a non-empty string.')
           
       
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self,last_name):
       if isinstance(last_name, str) and len(last_name):
           self._last_name = last_name
       else:
           raise ValueError('Lastname must be a non-empty string.')
     
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
       if isinstance(age, int) and 18 <= age <= 100:
           self._age = age
       else: 
           raise ValueError('Age must be an integer between 18 and 100 inclusive.')
    @property
    def symptoms(self):
        return self._symptoms
    @symptoms.setter
    def symptoms(self,symptoms):
       if isinstance(symptoms, list):
           self._symptoms = symptoms
       else:
           raise ValueError('Symptoms must be a list.')
       
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY,
            name TEXT,
            last_name TEXT,
            age INTEGER,
            symptoms TEXT
            )
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS patients
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = '''
             INSERT INTO patients(name, last_name, age, symptoms)
             VALUES(?,?,?,?)
        '''

        symptoms_str = ', '.join(self.symptoms)
        CURSOR.execute(sql,(self.name, self.last_name, self.age,  symptoms_str))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, last_name,  age, symptoms=None):
        patient = cls(name, last_name, age, symptoms)
        patient.save()
        return patient
    
    def update(self):
        sql = '''
             UPDATE patients
             SET name = ?, last_name= ?, age = ?,symptoms = ?
             WHERE id = ?
        '''
        symptom_str = ', '.join(self.symptoms)
        CURSOR.execute(sql, (self.name, self.last_name, self.age, symptom_str, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
             DELETE FROM patients
             WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        del type(self).all[self.id] 
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        patient = cls.all.get(row[0])
        symptom_list = row[4].split(', ') if row[4] else []
        if patient:
            patient.name = row[1]
            patient.last_name = row[2]
            patient.age = row[3]
            patient.symptoms = symptom_list
        else:
            patient = cls(row[1], row[2], row[3], symptom_list)
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient
    
    @classmethod
    def get_all(cls):
        patients = []
        sql = '''
             SELECT *
             FROM  patients
        '''
        rows = CURSOR.execute(sql).fetchall()
        for row in rows:
            patient = cls.instance_from_db(row)
            patients.append(patient)
        return patients
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
             SELECT * 
             FROM patients
             WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_last_name(cls, last_name):
        sql = '''
             SELECT *
             FROM patients
             WHERE last_name = ?
        '''
        row = CURSOR.execute(sql, (last_name, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def get_symptoms(self):
        symptoms_list = []
        from models.symptom import Symptom
        sql = '''
             SELECT *
             FROM symptoms
             WHERE patient_id = ?
        '''
        rows = CURSOR.execute(sql, (self.id, )).fetchall()
        for row in rows:
            symptom = Symptom.instance_from_db(row)
            symptoms_list.append(symptom)
        return  symptoms_list
    
    

    
     



   



    