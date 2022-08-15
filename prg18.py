#Program to find the maximum of three numbers.

# COMMON CODE

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))
c = int(input("Enter the Third Number : "))

def maximum(a, b, c):
    if a > b and a > c:
        print(f'{a} is greatest')
    if b > a and b > c:
        print(f'{b} is greatest')
    if c > b and c > a:
        print(f'{c} is greatest')

maximum(a, b, c)

# RECURSION

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))
c = int(input("Enter the Third Number : "))

def maximum(a, b, c):
    print(f'{max(a, b, c)} is greatest')

maximum(a, b, c)

# comment out one part which is not in use else you might get an error
