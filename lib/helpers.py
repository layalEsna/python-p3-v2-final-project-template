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
    try:
        new_patient = Patient.create(name, last_name, age)
        print(f'Success: {new_patient}')
    except Exception as e:
        print(f'Error: {e}')

def update_patient_by_id():
    id_ = input("enter patien's id: ")
    if id_:
        patient = Patient.find_by_id(id_)
        if patient:
            name = input("Enter patient's name: ")
            last_name = input("Enter patient's last name: ")
            age = input("Enter patient's age: ")
            try:
               patient.name = name
               patient.last_name = last_name
               patient.age = int(age)
               patient.update()
               print(f'Success<{patient.name} {patient.last_name} with id: {patient.id}, age: {patient.age}>')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print('Failed to update patient.')
    else:
        print(f'Patient with ID {id_} not found')

def update_patient_by_name():
    last_name = input("Enter patient's name: ")
    patient = Patient.find_by_last_name(last_name)
    if patient:
        name = input("Update patient's name: ")
        last_name = input("Update patient's last name: ")
        age = input("Update patient's age: ")
        try:
            patient.name = name
            patient.last_name = last_name
            patient.age = int(age)
            patient.update()
            print(f'Success<{patient.name} {patient.last_name} with ID: {patient.id}, age: {patient.age} updated.>')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print(f'Patient with last name {last_name} not found.')

def delete_by_id():
    id_ = input("Enter patient's ID: ")
    if id_:
        patient = Patient.find_by_id(id_)
        if patient:
            try:
                patient.delete()
                print(f'Success<Patient with ID {patient.id} has been deleted.>')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print(f'Patient with ID {id_} not found')
    else:
        print('No ID provided.')

def find_disease_by_name():
    name = input("Entere disease's name: ")
    disease = Disease.find_by_name(name)
    if disease:
        print(f'Found disease: {disease}')
    else: 
        print(f'{name} not found.')
    
def find_disease_by_id():
    id_ = input("Enter disease's ID: ")
    disease = Disease.find_by_id(id_)
    if disease:
        print(f'Disease by ID {id_} found')
    else:
        print(f'Disease by ID {id_} not found')

def delete_disease_by_id():
    id_ = input("Enter diseas's ID: ")
    disease = Disease.find_by_id(id_)
    if disease:
        try:
            disease.delete()
            print(f'Success<Disease {disease.name} with ID {id_} deleted.>')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print(f'Disease with ID {id_} not found.')

def update_disease_by_id():
    id_ = input("Enter disease's ID: ")
    if id_:
        disease = Disease.find_by_id(id_)
        if disease:
            name = input(f"Enter diseas's name: ")
            symptoms = input(f"Enter diseas's  symptoms (comma-separated): ")
            symptom_list = symptoms.split(', ') if symptoms else disease.symptoms
            try:
                disease.name = name
                disease.symptoms = symptom_list
                disease.update()
                print(f'Success<Disease with ID {id_} updated.>')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print(f'Disease with ID {id_} not found')
    else:
        print('ID did not provided.')


            