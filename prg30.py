# File Handling in Python
# Reading a file or "rb+" mode
import pickle
f = open("demo.dat", "rb+")
a = f.read()
print(f'Text initially : {a}')
pickle.dump("Hello user....", f)
print("Writing Done.......")
f.close()

