# Python program to implement stack using list

# Created an empty list named stack
stack = []

# PUSH operation
def PUSH():
    rng = int(input("Enter the number of elements to be added to the stack : "))
    for i in range(rng):
        element = int(input("Enter the element : "))
        stack.append(element)

# POP operation
def POP():
    print(f"Initial stack : {stack}")
    stack.pop()
    print(f"Updated stack")    

# Checking status of stack
def status():
    print("========== MENU ==========\n",
          "1. Top element\n",
          "2. Empty or not",)
    ch = int(input("Enter the choice : "))
    if ch == 1:
        print(f"Top element of the stack is {stack[-1]}")
    elif ch == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
            print(f"Stack is {stack}")

def main():
    print("========== MENU ==========\n",
          "1. PUSH operation\n",
          "2. POP operation\n",
          "3. Display the stack\n",
          "4. Check the status of stack")
    while True:
        choice = int(input("Enter the choice : "))
        if choice == 1:
            PUSH()
        elif choice == 2:
            POP()
        elif choice == 3:
            print(f"Stack : {stack}")
        elif choice == 4:
            status()

main()