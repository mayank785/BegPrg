# Python program to read a text file line by line and display each word seperated by "#"

f = open("demo.txt", "r")
for word in f.read():
    print(word.strip(), end = '#')
input()
f.close()