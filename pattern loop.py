#1
n=int(input("Enter a value for pattern"))
#
# for i in range(n):
#     for j in range(n+3):
#         print("*",end="")
#     print("*")

#2. Triangle pattern

for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

#3
# for i in range(n):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for j in range(2*(n-i)+1):
#         print("*",end=" ")
#     print()

#4
# num=0
# for i in range(10):
#     for j in range(i+1):
#         num+=1
#         print(num,end=" ")
#     print()

# #5
# n=65
# for i in range(10):
#     for j in range(n,n+i):
#         print(chr(j),end=" ")
#     print()

# #6
# n=65
# for i in range(27):
#     for j in range(n,n+i):
#         if j%2==0:
#          print(chr(j),end=" ")
#     print()

#7
# n=65
# for i in range(5):
#     for j in range(i,27):
#         print(" ",end=" ")
#     for j in range(n+i,n-1,-1):
#             print(chr(j),end=" ")
#     print()
#8
