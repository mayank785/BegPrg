# Program to search a record by roll number and print all details from a binary file

import pickle
f = open("student.dat", "rb")
stud_rec = pickle.load(f)
found = 0
roll_no = int(input("Enter the roll number for search : "))
for R in stud_rec:
    if R[0] == roll_no:
        print(f"Success, roll number : {roll_no} found !")
        print("Details")
        print(f"Roll number : {R[0]}")
        print(f"Name : {R[1]}")
        print(f"Marks : {R[2]}")
    found = 1
    break
if found == 0:
    print("Sorry record not found...")
f.close()
