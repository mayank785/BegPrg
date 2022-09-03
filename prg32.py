# File Handling in Python
# Reading a file or "wb" mode
import pickle
f = open("demo.dat",  "wb")
pickle.dump("Hello", f)
print("Writing Done........")
f.close()
