# This is a simple CLI-based notepad application.
# It can create, open, append and save text files. 

import os

def show_welcome_message():
    print("\n********** Welcome to my Notepad **********\n")

def show_menu():
    print("------- Menu --------")
    print("1. Create a new note")
    print("2. Read a note")
    print("3. Append to a note")
    print("4. Delete a note")
    print("5. Exit")

def create_note():
    filename = input("Enter the filename to create: ").strip()
    if filename:
        print("Start typing your note (type SAVE to finish): ")
        content = ''

        while True:
            user_input = input()
            if user_input.lower() == "save":
                break
            content += user_input + "\n"

        with open(filename, 'w') as file:
            file.write(content)
            print(f"Your note has been saved in file '{filename}'.")
    else:
        print("Filename cannot be empty")

def read_note():
    filename = input("Enter the filename to read: ").strip()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(f"------ Contents of {filename} ------")
            content = file.read()
            if not content:
                print("The note is empty.")
            else:
                print(content)

    else:
        print("File does not exist.")

def append_note():
    filename = input("Enter the filename to append: ").strip()

    if os.path.exists(filename):
        with open(filename, "a") as file:
            print("Start adding to your note (type SAVE to finish.)")
            content = ''

            while True:
                user_input = input()
                if user_input.lower() == "save":
                    break
                content += user_input + "\n"

            file.write(content)
            print("Your note has been appended.")

    else:
        print("File does not exist.")

def delete_note():
    filename = input("Enter the filename to delete: ").strip()

    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"'{filename}' has been deleted successfully.")
        
        except FileNotFoundError:
            print("File does not exist.")
            
        except PermissionError:
            print("Permission denied: Cannot delete this file.")
            
        except Exception as e:
            print(f"Unexpected error: {e}")

    else:
        print("File does not exist.")
    
def close_program():
    print("See you next time.")
    exit()

while True:
    show_welcome_message()
    show_menu()

    choice = input("Enter your choice: ")

    if choice == '5':
        close_program()

    elif choice == '1':
        create_note()

    elif choice == '2':
        read_note()   

    elif choice == '3':
        append_note()
    
    elif choice == '4':
        delete_note()
           
    else:
        print("Wrong input! Choose again!!")