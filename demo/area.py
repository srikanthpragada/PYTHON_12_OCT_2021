obj_type = input("Enter object [c/s/r] :")

if obj_type == 'c':
    r = float(input("Enter radius :"))
    print(3.14 * r * r)
elif obj_type == 's':
    side = float(input("Enter side :"))
    print(side * side)
else:
    width = float(input("Enter width :"))
    length = float(input("Enter length :"))
    print(width * length)
