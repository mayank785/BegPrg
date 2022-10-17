# Python program to read a text file and display the number of vowels and consonants characters in a file

vowels = 0
consonants = 0

f = open("demo.txt", "r")
for characters in f.read():
    if characters.lower() in "aeiou":
        vowels += 1
    elif characters.lower() not in "aeiou":
        consonants += 1
        
print(f"Vowels : {vowels}")
print(f"Consonants : {consonants}")

f.close()