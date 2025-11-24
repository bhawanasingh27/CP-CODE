# Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle)

a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))
if a + b + c == 180 or a <= 0 or b <= 0 or c <= 0:
    print("valid triangle angles!")
else:
    
    if a == 90 or b == 90 or c == 90:
        print("Right Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")

