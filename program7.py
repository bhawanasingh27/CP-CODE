a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c != 180:
    print("Not a triangle")
elif 90 in (a, b, c):
    print("Right triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse triangle")
else:
    print("Acute triangle")
