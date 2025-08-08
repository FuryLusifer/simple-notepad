# This is a simple CLI-based notepad application.
# It can create, open, append and save text files. 

import os


class SimpleNotepad:
    def show_welcome_message(self):
        print("\n********** Welcome to my Notepad **********\n")

    def show_menu(self):
        print("------- Menu --------")
        print("1. Create a new note")
        print("2. Read a note")
        print("3. Append to a note")
        print("4. Delete a note")
        print("5. Exit")

    def create_note(self):
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

    def read_note(self):
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

    def append_note(self):
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

    def delete_note(self):
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
        
    def close_program(self):
        print("See you next time.")
        exit()

my_notepad = SimpleNotepad()

while True:
    my_notepad.show_welcome_message()
    my_notepad.show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        my_notepad.create_note()

    elif choice == '2':
        my_notepad.read_note()   

    elif choice == '3':
        my_notepad.append_note()
    
    elif choice == '4':
        my_notepad.delete_note()

    elif choice == '5':
        my_notepad.close_program()
           
    else:
        print("Wrong input! Choose again!!")