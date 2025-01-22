#area of triangle using HERONS FORMULA

a=int(input("enter first side of triangle"))
b=int(input("enter second side of triangle"))
c=int(input("enter third side of triangle"))

s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is ",area)