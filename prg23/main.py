import findArea

shape = input("Enter the shape of whose you want to calculate area : ")
if shape == "square":
    s = int(input("Enter the side (in m) : "))
    area = findArea.sq_ar(s)
    print(f'Area of the square = {area} sq. m')

elif shape == "rectangle":
    l = int(input("Enter the length (in m) : "))
    w = int(input("Enter the width (in m) : "))
    area = findArea.rec_ar(l, w)
    print(f'Area of the rectangle = {area} sq. m')

elif shape == "circle":
    r = int(input("Enter the radius (in m) : "))
    area = findArea.cir_ar(r)
    print(f'Area of the circle = {area} sq. m')

elif shape == "triangle":
    b = int(input("Enter the base (in m) : "))
    h = int(input("Enter the height (in m) : "))
    area = findArea.tri_ar(b, h)
    print(f'Area of the triangle = {area} sq. m')
