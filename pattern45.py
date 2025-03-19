#1. VALUE OF nCr
# n=int(input("Enter the value of n:"))
# r=int(input("Enter the value of r:"))
# factn=1
# factr=1
# factnr=1
# if r>n:
#     print("Invalid input")
# else:
#     for i in range(1,n+1):
#         factn=factn*i
#     print(factn)
#     for i in range(1,r+1):
#         factr=factr*i
#     print(factr)
#     for i in range(1,n-r+1):
#         factnr=factnr*i
#     print(factnr)
# print(factn/(factr*factnr))

#2.PASCAL TRIANGLE
# row=int(input("Enter Row: "))
# for i in range(row):
#     for j in range(i+1,row):
#         print(" ",end="")
#     value =1
#     for j in range(i+1):
#         print(value,end=" ")
#         value = value*(i-j)//(j+1)
#     print()

#3.
# n=65
# for i in range(5):
#     for j in range(i,5):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(n),end=" ")
#         n+=1
#     print()

#4.
# for i in range(5):
#     for j in range(i,5):
#         print("*", end="")
#     for j in range(i):
#         print(" ", end="")
#     for j in range(i):
#         print(" ", end="")
#     for j in range(i,5):
#         print("*", end="")
#     print()

#5
n=int(input("Enter a terms value: "))
p=64
for i in range(n):
    for j in range(i,n):
        p+=1
        print(chr(p), end="")
    for j in range(i):
        print(" ", end="")
    for j in range(i):
        print(" ", end="")
    for j in range(i,n):
        print(chr(p), end="")
        p-=1
    print()

