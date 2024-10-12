# lib/cli.py
import sqlite3
CONN = sqlite3.connect('medical_records.db')
CURSOR = CONN.cursor()


from helpers import (
    exit_program,
    helper_1
)


def main():
    try:
 
  
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                helper_1()
            else:
                print("Invalid choice")
    finally:
        CURSOR.close()
        CONN.close()


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
