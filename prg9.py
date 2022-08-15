# input the base and height of triangle and print its area (using user - defined function)

h = int(input("Enter the height of the triangle : "))
b = int(input("Enter the base of the triangle : "))
def ar_tri(h, b):
    area = (b * h)/2
    print(f"Area : {area}")

ar_tri(h, b)
