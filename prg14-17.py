# types of arguments
"""
1. positional arg
2. default arg
3. keyword arg
4. variable len arg
"""
# prg14
def sub(a, b):
    print(a - b)

# prg15
def msg(nm = "user"):
    print(f"Welcome {nm}!")

# prg16
def avg(a, b, c = 10):
    return (a + b + c) / 3

# prg17
def add(*n):
    total = 0
    for i in n:
        total += i
    print(f"Sum is : {total}")
