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

