# This is a simple CLI-based notepad application.
# It can create, open, append and save text files. 

import os

# A welcome message
print("\n********** Welcome to my Notepad **********\n")

def show_menu():
    print("------- Menu --------")
    # Available Menu
    print("1. Create a new note")
    print("2. Read a note")
    print("3. Append to a note")
    print("4. Delete a note")
    print("5. Exit")

# looping to keep showing the menu and taking user choice.
while True:
    # showing the menu
    show_menu()

    # Asking for user choice
    choice = input("Enter your choice: ")

    # acting on user choices
    if choice == '5':
        print("See you next time.")
        break


    elif choice == '1':
        # print("You chose option 1.")
        filename = input("Enter the filename to create: ").strip()
        if not filename:
            print("filename cannot be empty!!!\n")
            continue

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

    
    elif choice == '2':
        # print("You chose option 2.")
        filename = input("Enter the filename to read: ").strip()
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                print(f"------ Contents of {filename} ------")
                content = file.read()
                if not content:
                    print("The note is empty.")
                else:
                    print(f"\n{content}")
                print()
        else:
            print("File does not exist.")


    elif choice == '3':
        # print("You chose option 3.")
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
                print("Your note has been saved.")

        else:
            print("File does not exist.")

    
    elif choice == '4':
        # print("You chose option 4.")
        filename = input("Enter the filename to delete: ").strip()

        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"'{filename}' has been deleted successfully.")
            
            except PermissionError:
                print("Permission denied: Cannot delete this file.")
            
            except Exception as e:
                print(f"Unexpected error: {e}")

        else:
            print("File does not exist.")    
    else:
        print("Wrong input! Choose again!!")
    
    # adding a empty line
    print()
