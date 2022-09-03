# File Handling in Python
# Reading a file or "a+" mode

f = open("demo.txt", "a+")
f.write("\nBye...")
print("Writing Done......")
f.seek(0)
a = f.read()
print(f'Content : {a}')
f.close()
