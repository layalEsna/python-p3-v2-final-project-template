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