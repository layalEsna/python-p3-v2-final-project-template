# lib/models/disease.py
from lib.cli import CONN, CURSOR

class Disease:
    all = {}
    def __init__(self, name, symptoms=None, id=None):
       self.id = id
       self.name = name
       self.symptoms = symptoms or []
      

    def __repr__(self):
        return (
            f'<Disease {self.id}: {self.name}>'
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
             CREATE TABLE IF NOT EXISTS diseases(
             id INTEGER PRIMARY KEY, name TEXT, symptoms TEXT
             )
        '''
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS diseases
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = '''
             INSERT INTO diseases(name, symptoms)
             VALUES(?,?)
        '''
        symptoms_str = ', '.join(self.symptoms)
        CURSOR.execute(sql, (self.name, symptoms_str))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, symptoms=None):
        disease = cls(name, symptoms)
        disease.save()
        return disease
    
    def update(self):
        symptoms_str = ', '.join(self.symptoms)
        sql = '''
             UPDATE diseases
             SET name = ?, symptoms = ?
             WHERE id = ?
             
        '''
        CURSOR.execute(sql, (self.name,symptoms_str, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
             DELETE FROM diseases
             WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        disease = cls.all.get(row[0])
        symptom_list = row[2].split(', ') if row[2] else []
        if disease:
              disease.name = row[1]
              disease.symptoms =  symptom_list
        else:
            disease = cls(row[1],  symptom_list)
            disease.id = row[0]
            cls.all[disease.id] = disease
        return disease
    
    @classmethod
    def get_all(cls):
        diseases = []
        sql = '''
             SELECT *
             FROM diseases
        '''
        rows = CURSOR.execute(sql).fetchall()
        for row in rows:
            disease = cls.instance_from_db(row)
            diseases.append(disease)
        return diseases
    @classmethod
    def find_by_id(cls, id):
        sql = '''
             SELECT *
             FROM diseases
             WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = '''
             SELECT * 
             FROM diseases
             WHERE name = ?
        '''
        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.instance_from_db(row) if row else None






    



