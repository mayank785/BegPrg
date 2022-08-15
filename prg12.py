# using an equation and some user - defined function, solving the equation

eq = "(2 + 3) - (2 - 1) x (2 x 3) + (12 / 2)"       # can use any other equation
print(f"Equation is : {eq}")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(add(2, 3) - sub(2, 1) * mul(2, 3) + div(12, 2))       # make sure you modify the values here if you are changing the equation above
