# Python program to create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.

import pickle
studList = {}

def writer():
    with open("studentList.dat", "ab") as studListBin:
        rng = int(input("Enter the number of records you want to add : "))
        for i in range(rng):
            studList["roll number"] = int(input("Enter the roll number : "))
            studList["name"] = input("Enter the name : ")
            pickle.dump(studList, studListBin)
            
def display():
    with open("studentList.dat", "rb") as studListBin:
        try:
            while True:
                content = pickle.load(studListBin)
                print(content)
        except EOFError:
            pass

def search():
    success = 0
    rollNumberToSearch = int(input("Enter the roll number to search : "))
    with open("studentList.dat", "rb") as studListBin:
        try:
            while True:
                content = pickle.load(studListBin)
                if content["roll number"] == rollNumberToSearch:
                    print(content)
                    success = 1
        except EOFError:
            print("Record not found...")

def main():
    print("========== MENU ==========\n",
          "1. Insert record\n",
          "2. Display\n",
          "3. Search\n")
    while True:
        choice = int(input("Enter the choice : "))
        if choice == 1:
            writer()
        elif choice == 2:
            display()
        elif choice == 3:
            search()
        
main()