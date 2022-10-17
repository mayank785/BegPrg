# Python program to create a binary file with roll number, name, and marks. Update the marks using roll number

import pickle
marksList = {}

def writer():
    with open("marksList.dat", "ab") as marksListBin:
        rng = int(input("Enter the number of records to be added : "))
        try:
            for i in range(rng):
                marksList["roll number"] = int(input("Enter the roll number : "))
                marksList["name"] = input("Enter the name : ")
                marksList["marks"] = int(input("Enter the marks : "))
                pickle.dump(marksList, marksListBin)
        except EOFError:
            pass

def updater():
    with open("marksList.dat", "rb") as marksListBin:
        rollNumberToSearch = int(input("Enter the roll number to be searched : "))
        try:
            while True:
                data = pickle.load(marksListBin)
                if data["roll number"] == rollNumberToSearch:
                    print("Record Found...")
                    print(data)
                    newMarks = int(input("Enter the marks : "))
                    data["marks"] = newMarks
                    print("Marks updated...")
                    print(data)
                else:
                    print("Record not found...")
        except EOFError:
            pass

def main():
    print("========== MENU ==========\n",
          "1. Insert record\n",
          "2. Update Marks\n",)
    while True:
        choice = int(input("Enter the choice : "))
        if choice == 1:
            writer()
        elif choice == 2:
            updater()

main()