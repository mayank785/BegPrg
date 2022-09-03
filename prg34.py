# File Handling in Python
# Reading a file or "wb+" mode
import pickle
f = open("demo.dat",  "wb+")
pickle.dump("Hello user", f)
print("Writing Done........")
f.seek(0)
a = f.read()
print(f'Content : {a}')
f.close()
