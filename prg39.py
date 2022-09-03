# File Handling in Python
# Binary files

import pickle
f = open("demo.dat", "rb")
d = pickle.load(f)
f.close()
print(d)
