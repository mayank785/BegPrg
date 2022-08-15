#Program to remove the 'n'th index of the non-empty string

string = input("Enter the string : ")
new_string = ''
n = int(input("Enter the index : "))
for i in range(len(string)):
    if n != i:
        new_string += string[i]
        i += 1
    elif n == i:
        i += 1
print(new_string)
