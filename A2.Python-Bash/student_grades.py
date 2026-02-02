
Student_data = {
    "Aman" : 'A',                      # student marks data in dict
    "Aayush" : 'B',             
    "Karan" : 'F',
    "Monisha" : 'D',
    "Yash" : 'C'
}

while(True):
    print("\n1. Add new student data\n2. Update student grades\n3. Print student data\n4. Press any key to exit...")
    user_input = int(input("\nEnter a number to choose: "))

    if user_input == 1 or user_input == 2:
        new_data = input("Enter the student name: ")
        new_grade = input("Enter student grade: ")
        Student_data[new_data] = new_grade

    elif user_input == 3:
        print(Student_data)
    else:
        print("\nExiting...\n")
        break
