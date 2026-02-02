marks = int(input("Enter marks scored by student: "))

while(True):
    if marks <=100 and marks >=0:
        break
    else:
        marks = int(input("Invalid Marks! Re-Enter marks scored by student: "))


if marks >= 90:
    result = 'A'
elif marks >= 80:
    result = 'B'
elif marks >= 70:
    result = 'C'
elif marks >= 60:
    result = 'D'
else: 
    result = 'F'

print("Grade Achieved by student is: "+ result)    