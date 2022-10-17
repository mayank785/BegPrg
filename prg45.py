# Menu driven python program to create a stack, use PUSH and POP operations, and also display the stack

stack = []
c = 'y'
while (c.lower() == 'y'):
    print("1 to PUSH\n2 to POP\n3 to Display")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        a = input("Enter any number : ")
        stack.append(a)
    elif choice == 2:
        if (stack == []):
            print("Stack is empty")
        else:
            print(f"Deleted element is : {stack.pop()}")
    elif choice == 3:
        l = len(stack)
        for i in range(l - 1, -1, -1):
            print(stack[i])
    else:
        print("Wrong input")
    c = input("Want to continue or not (y or n) : ")