# This is a simple CLI-based notepad application.
# It allows users to create, read, append, and delete text notes via the command line.

import os

class SimpleNotepad:
    """
    A simple command-line notepad application.
    Provides functionality to create, read, append, and delete text notes.
    """
    def show_welcome_message(self):
        """
        Displays a welcome message to the user when the program starts.
        """
        print("\n********** Welcome to my Notepad **********\n")

    def show_menu(self):
        """
        Displays the main menu with available options to the user.
        """

        print("------- Menu --------")
        print("1. Create a new note")
        print("2. Read a note")
        print("3. Append to a note")
        print("4. Delete a note")
        print("5. Exit")

    def run_notepad(self):
        """
        Runs the main loop of the notepad application.
        Handles user input and calls the appropriate methods based on the menu choice.
        """
        while True:
            my_notepad.show_menu()
            choice = input("Enter your choice: ").strip()

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

    def create_note(self):
        """
        Creates a new note file.
        Prompts the user for a filename and note content, then saves it to disk.
        """
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
        """
        Reads and displays the contents of a specified note file.
        """
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
        """
        Appends additional content to an existing note file.
        """
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
        """
        Deletes a specified note file from disk.
        Handles errors such as file not found or permission denied.
        """
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
        """
        Exits the notepad application gracefully.
        """
        print("See you next time.")
        exit()


# Create an instance of SimpleNotepad and start the application
my_notepad = SimpleNotepad()
my_notepad.show_welcome_message()
my_notepad.run_notepad()