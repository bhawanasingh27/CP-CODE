angle1=int(input("enter angle1 :"));
angle2=int(input("enter angle2 :"));
angle3=int(input("enter angle3 :"));
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0 :
    print("Valid triangle")
else:
    print("not valid triangle");