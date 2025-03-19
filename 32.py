#WAP to check triangle condition

l1=int(input("Enter first side of triangle"))
l2=int(input("Enter second side of triangle"))
l3=int(input("Enter third side of triangle"))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print("The triangle is perfect")
else:
    print("The triangle is not perfect")

