# lib/models/patient.py
from lib.cli import CONN, CURSOR

class Patient:
    all = {}
    def __init__(self, name, last_name, age , id=None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        

    def __repr__(self):
        return (
        f'<Patient {self.id}: {self.name}, {self.last_name}, {self.age}>'
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
    # @property
    # def symptoms(self):
    #     return self._symptoms
    # @symptoms.setter
    # def symptoms(self,symptoms):
    #    if isinstance(symptoms, list):
    #        self._symptoms = symptoms
    #    else:
    #        raise ValueError('Symptoms must be a list.')
       
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY,
            name TEXT,
            last_name TEXT,
            age INTEGER
          
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
        '''Insert the Patient instance into the database and save the ID.
'''
        sql = '''
             INSERT INTO patients(name, last_name, age)
             VALUES(?,?,?)
        '''
        CURSOR.execute(sql,(self.name, self.last_name, self.age))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, last_name,  age):
        '''Create and save a new Patient instance.'''
        patient = cls(name, last_name, age)
        patient.save()
        return patient
    
    def update(self):
        '''Update an existing Patient record in the database.'''
        sql = '''
             UPDATE patients
             SET name = ?, last_name= ?, age = ?
             WHERE id = ?
        '''
       
        CURSOR.execute(sql, (self.name, self.last_name, self.age, self.id))
        CONN.commit()

    def delete(self):
        '''Delete the Patient record from the database.'''
       
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
        '''Return a Patient instance based on a database row.'''
        patient = cls.all.get(row[0])
        if patient:
            patient.name = row[1]
            patient.last_name = row[2]
            patient.age = row[3]
            
        else:
            patient = cls(row[1], row[2], row[3])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient
    
    @classmethod
    def get_all(cls):
        '''Return a list of all Patient instances from the database.'''
        
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
        '''Find and return a Patient instance by ID.'''
        sql = '''
             SELECT * 
             FROM patients
             WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_last_name(cls, last_name):
        '''Find and return a Patient instance by last name.'''
        sql = '''
             SELECT *
             FROM patients
             WHERE last_name = ?
        '''
        row = CURSOR.execute(sql, (last_name, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    # def get_symptoms(self):
    #     symptoms_list = []
    #     from models.symptom import Symptom
    #     sql = '''
    #          SELECT *
    #          FROM symptoms
    #          WHERE patient_id = ?
    #     '''
    #     rows = CURSOR.execute(sql, (self.id, )).fetchall()
    #     for row in rows:
    #         symptom = Symptom.instance_from_db(row)
    #         symptoms_list.append(symptom)
    #     return  symptoms_list
              

        
    
    

    
     



   



    