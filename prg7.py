# input length and breadth of rectangle and print its area (using user - defined function)

l = int(input("Enter the length of the rectangle : "))
b = int(input("Enter the breadth of the rectangle : "))
def ar_rec(l, b):
    area = l * b
    print(f"Area : {area}")

ar_rec(l, b)
