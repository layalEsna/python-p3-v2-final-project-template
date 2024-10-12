# lib/models/symptom.py
from lib.cli import CONN, CURSOR

class Symptom:
    all = {}

    def __init__(self, description, patient_id, disease_id, id=None):
        self.id = id
        self.description = description
        self.patient_id = patient_id
        self.disease_id = disease_id

    def __repr__(self):
        return (
            f'<symptom {self.id}: {self.description}, '+
            f'Patient ID: {self.patient_id}, Disease ID: {self.disease_id}>'
        )
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self,description):
       if isinstance(description, str) and 30<= len(description)<= 500:
           self._description = description
       else:
           raise ValueError('description must be between 30 and 500 characters inclusive.')
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS symptoms(
            id INTEGER PRIMARY KEY, description TEXT, FOREIGN KEY (patient_id) REFERENCES patients(id), FOREIGN KEY (disease_id) REFERENCES diseases(id)
            )
        '''
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql = '''
             DROP TABLE IF EXISTS symptoms
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = '''
             INSERT INTO symptoms(description, patient_id, disease_id) 
             VALUES(?,?,?)  
        '''
        CURSOR.execute(sql, (self.description, self.patient_id, self.disease_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, description, patient_id, disease_id):
        symptom = cls(description, patient_id, disease_id)
        symptom.save()
        return symptom
    
    def update(self):
        sql = '''
             UPDATE symptoms
             SET description = ?, patient_id = ?, disease_id = ?
             WHERE id = ?
        '''
        CURSOR.execute(sql, (self.description, self.patient_id, self.disease_id, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
             DELETE FROM symptoms
             WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod 
    def instance_from_db(cls, row):
       symptom = cls.all.get(row[0])
       if symptom:
           symptom.description = row[1]
           symptom.patient_id = row[2]
           symptom.disease_id = row[3]
       else:
           symptom = cls(row[1], row[2], row[3])
           symptom.id = row[0]
           cls.all[symptom.id] = symptom
       return symptom
    
    @classmethod
    def get_all(cls):
        symptoms = []
        sql = '''
             SELECT *
             FROM symptoms
        '''
        rows = CURSOR.execute(sql).fetchall()
        for row in rows:
            symptom = cls.instance_from_db(row)
            symptoms.append(symptom)
        return symptoms
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
             SELECT *
             FROM symptoms
             WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_description(cls, description):
        sql = '''
             SELECT *
             FROM symptoms
             WHERE description = ?
        '''
        row = CURSOR.execute(sql, (description, )).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_patient_id(cls, patient_id):
        patient_symptoms = []
        sql = '''
             SELECT *
             FROM symptoms
             WHERE patient_id = ?
        '''
        rows = CURSOR.execute(sql, (patient_id, )).fetchall()
        for row in rows:
            symptom = cls.instance_from_db(row)
            patient_symptoms.append(symptom)
        return patient_symptoms if patient_symptoms else None
