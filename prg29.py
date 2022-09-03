# File Handling in Python
# Reading a file or "r+" mode

f = open("demo.txt", "r+")
a = f.read()
print(f'Text initially : {a}')
f.write("Hello")
print("Writing Done..............")
f.close()
