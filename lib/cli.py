# lib/cli.py
import sqlite3
CONN = sqlite3.connect('medical_records.db')
CURSOR = CONN.cursor()


from helpers import (
    exit_program,
    helper_1,
    list_patients,
    list_diseases,
    list_symptoms,
    add_new_patient,
    update_patient_by_id,
    update_patient_by_name,
    delete_by_id,
    find_disease_by_name,
    find_disease_by_id,
    delete_disease_by_id,
    update_disease_by_id,
)


def main():
    try:
 
  
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                list_patients()
            elif choice == "2":
                add_new_patient()
            elif choice == "3":
                update_patient_by_id()
            elif choice == "4":
                update_patient_by_name()
            elif choice == "5":
                delete_by_id()
            elif choice == "6":
                list_diseases()
            elif choice == "7":
                find_disease_by_name()
            elif choice == "8":
                find_disease_by_id()
            elif choice == "9":
                update_disease_by_id()
            elif choice == "10":
                delete_disease_by_id()
            elif choice == "11":
                list_symptoms()
            else:
                print("Invalid choice")
    finally:
        CURSOR.close()
        CONN.close()


def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. List all patients")
    print("2. Add a new patient")
    print("3. Update patient by ID")
    print("4. Update patient by last name")
    print("5. Delete patient by ID")
    print("6. List all diseases")
    print("7. Find disease by name")
    print("8. Find disease by ID")
    print("9. Update disease by ID")
    print("10. Delete disease by ID")
    print("11. List all symptoms")

if __name__ == "__main__":
    main()
