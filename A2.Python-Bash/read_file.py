def fileRead():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, "r") as file:           # using r if file already exists
            print(file.read())
    except FileExistsError:
        print("Error: The file " + filename + " doesnt't exists.")

    print("Successfully read to " + filename + "!")

if __name__ == "__main__":
    fileRead()