# input the diameter of the sphere and print the volume of the sphere in litres

dia = int(input("Enter the diameter of sphere (in cm) : "))
radius = dia / 2
vol_cm3 = (4/3) * 3.14 * (radius ** 3)
vol_l = vol_cm3 / 1000
print(f"Volume of sphere of diameter {dia} is {vol_l} litres.")
