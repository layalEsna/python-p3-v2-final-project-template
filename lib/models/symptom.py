# lib/models/symptom.py

class Symptom:

    def __init__(self, description, patient_id, disease_id, id=None):
        self.id = id
        self.description = description
        self.patient_id = patient_id
        self.disease_id = disease_id

    def __repr__(self):
        return (
            f'<symptom {self.id}: {self.description}, '+
            f'Patient ID: {self.patient_id}, Disease ID: {self.patient_id}>'
        )