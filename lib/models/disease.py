# lib/models/disease.py

class Disease:
    def __init__(self, name,symptoms=None, id=None):
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


