# File Handling in Python
# Binary files

def binFile():
    import pickle
    f = open("data.dat", "wb")
    while True:
        x = int(input("Enter the number : "))
        pickle.dump(x, f)
        a = input("Want to add more data? (y or n) : ")
        if a.upper() == "N":
            break
    f.close()
    f = open("data.dat", "rb")
    try:
        while True:
            y = pickle.load(f)
            print(y)
    except EOFError:
        print("Somthing went wrong")
    f.close()
binFile()
