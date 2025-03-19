#FIBONACCI SERIES (0, 1, 1, 2, 3, 5, 8, 13)

n=int(input("Enter a terms "))
n1=0
n2=1

for i in range(n):
    print(n1,end=" ")
    n1,n2=n2,n1+n2
print()