# Python program to read a file and remove all the lines with letter 'a' in it and re-write the leftover lines in other file

ff = open("demo.txt", "r")
for line in ff.readlines():
    print(line.strip())
    if 'a' not in line:
        sf = open("new_demo.txt", "a")
        sf.write(line)
        sf.close()            
ff.close()
input()