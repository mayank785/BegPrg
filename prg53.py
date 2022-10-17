# Python program to create a CSV file by entering user id and password. Also search the password for given user id

useridList = {}

def listtocsv():
    global useridList
    for i in useridList:
        with open("userlist.csv", "a") as userList:
            userList.write(f'{i}, {useridList[i]}/n')   
    
def writer():
    with open("userlist.csv", "a") as userList:
        userid = input("Enter the userid : ")
        password = input("Enter the password : ")
        if userid not in useridList:
            useridList[userid] = password
            listtocsv()
            main()
        else:
            print(f"{userid} is already present in the list...")
            main()
  
def search():
    with open("userlist.csv", "r") as userList:
        userIdToBeSearched = input("Enter the userid to be searched : ")
        if userIdToBeSearched in useridList:
            print(f"Password for {userIdToBeSearched} is {useridList[userIdToBeSearched]}")
            main()
        else:
            print("Userid not found...")
            main()
    
def main():
    print("===== User ID and Password Manager =====")
    print("1. Add id and password\n",
        "2. Search any password")
    choice = int(input("Enter the choice : "))
    if choice == 1:
        writer()
    elif choice == 2:
        search()
main()
