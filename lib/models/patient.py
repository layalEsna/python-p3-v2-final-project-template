# lib/models/patient.py

class Patient:
    all = {}
    def __init__(self, name, age,symptoms=None, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.symptoms = symptoms or []

    def __repr__(self):
        return (
            f'<Patient {self.id}: {self.name}, {self.age}, ' + 
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

    