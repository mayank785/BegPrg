# File Handling in Python
# Reading a file or "ab" mode
import pickle
f = open("demo.dat", "ab")
pickle.dump("I am learning python", f)
print("Writing Done......")
f.close()
