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
        '''Create the symptoms table in the database.'''

        sql = '''
            CREATE TABLE IF NOT EXISTS symptoms(
            id INTEGER PRIMARY KEY, description TEXT,
            patient_id INTEGER,
            disease_id INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patients(id),
            FOREIGN KEY (disease_id) REFERENCES diseases(id)
            )
        '''
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        '''Drop the symptoms table from the database'''
        sql = '''
             DROP TABLE IF EXISTS symptoms
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        '''Insert the Symptom instance into the database and save the ID.'''
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
        '''Create and save a new Symptom instance.'''
        symptom = cls(description, patient_id, disease_id)
        symptom.save()
        return symptom
    
    def update(self):
        '''Update an existing Symptom record in the database.'''
        sql = '''
             UPDATE symptoms
             SET description = ?, patient_id = ?, disease_id = ?
             WHERE id = ?
        '''
        CURSOR.execute(sql, (self.description, self.patient_id, self.disease_id, self.id))
        CONN.commit()

    def delete(self):
        '''Delete the Symptom record from the database.'''
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
       '''Return a Symptom instance based on a database row.'''
        
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
        '''Return a list of all Symptom instances from the database.'''
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
        '''Find and return a Symptom instance by ID.'''
        sql = '''
             SELECT *
             FROM symptoms
             WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_description(cls, description):
        '''Find and return a list of Symptom instances by description.'''
        symptoms = []
        sql = '''
             SELECT *
             FROM symptoms
             WHERE description = ?
        '''
        rows= CURSOR.execute(sql, (description, )).fetchall()
        for row in rows:
            symptom = cls.instance_from_db(row) 
            symptoms.append(symptom)
        return symptoms if symptoms else None
    @classmethod
    def find_by_patient_id(cls, patient_id):
        '''Find and return a list of Symptom instances by patient ID.'''
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
