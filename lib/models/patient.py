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
    