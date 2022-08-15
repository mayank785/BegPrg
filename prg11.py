# input principle amount, rate of interest, time and print simple interest (using user - defined function)

p = int(input("Enter the principle amount : "))
r = int(input("Enter the rate of interest : "))
t = int(input("Enter the time : "))
def si(p, r, t):
    s = (p * r * t)/100
    print(f"Simple Interest : {s}")

si(p, r, t)
