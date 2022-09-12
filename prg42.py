# Program to input/append a record in binary file

import pickle
record = []
while True:
        roll_no = int(input("Enter the roll number : "))
        name = input("Enter the name : ")
        marks = int(input("Enter the marks : "))
        data = [roll_no, name, marks]
        record.append(data)
        choice = input("Want to enter more data ? (Y or N) : ")
        if choice.upper() == "N":
                break

f = open("student.dat", "wb")
pickle.dump(record, f)
print("Records added successfully!!!")
f.close()
