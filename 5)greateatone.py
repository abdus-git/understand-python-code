a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))

if a>b and a>c:
    print("a is greatest no.",a)
if b>c and b>a:
    print("b is greatest no.",b)
if c>a and c>b:
    print("c is greatest no.",c)

#To check the minimum value
    print("smallest no.",min(a,b,c))