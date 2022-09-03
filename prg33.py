# File Handling in Python
# Reading a file or "w+" mode

f = open("demo.txt",  "w+")
f.write("Hey guys!")
print("Writing Done........")
f.seek(0)
a = f.read()
print(f'Content : {a}')
f.close()
