# File Handling in Python
# Binary files

def fopr():
    import pickle
    l = [10, 20, 30,40]
    f = open("list.dat", "wb")
    pickle.dump(l, f)
    print("Success")
    f.close()
fopr()
