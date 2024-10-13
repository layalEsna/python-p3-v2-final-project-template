# lib/helpers.py
from models.patient import Patient
from models.disease import Disease
from models.symptom import Symptom

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
     
def list_patients():
    '''List all patients.'''
    patients = Patient.get_all() 
    if patients:
        for patient in patients:
            print(patient)
    else:
        print('No patients found.')

def list_diseases():
    '''List all diseases.'''
    diseases = Disease.get_all()
    if diseases:
        for disease in diseases:
            print(disease)
    else:
        print('No diseases found.')
  

def list_symptoms():
    '''List all symptoms.'''
    symptoms = Symptom.get_all()
    if symptoms:
        for symptom in symptoms:
            print(symptom)
    else:
        print('No symptoms found.')

def add_new_patient():
    name = input("Enter the patient's name: ")
    last_name = input("Enter the patient's last_name: ")
    age = input("Enter the patient's age: ")
    symptoms_list = input("Enter the patient's symptoms (comma-separated): ").split(',')
    try:
        new_patient = Patient.create(name, last_name, age)
        print(f'Success: {new_patient}')
    except Exception as e:
        print(f'Error: {e}')

        for synptom in symptoms_list:
            
   
    