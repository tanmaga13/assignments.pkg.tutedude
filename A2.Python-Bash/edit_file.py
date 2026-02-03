
def fileCreate():
    while True:    
        print("1. Create a new file")
        print("2. Write/Overwrite a file")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == '1':
            filename = input("Enter the filename to create: ")
            try:
                with open(filename, "x") as file:           # using x if file already exists
                    print(f"File '{filename}' created successfully.")
            except FileExistsError:
                print(f"Error: The file '{filename}' already exists.")

        elif choice == '2':
            filename = input("Enter the filename to write to: ")
            content = input("Enter the text you want to save: ")

            with open(filename, "w") as file:   # using 'w' to write in file
                file.write(content)
            print("Successfully wrote to '{filename}'.")

        else:
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    fileCreate()