# input the radius of circle and print its area (using user - defined function)

r = int(input("Enter the radius of the circle : "))
def ar_cir(r):
    area = 3.14 * (r ** 2)
    print(f"Area : {area}")

ar_cir(r)
