##1.
# Fruits=["Kela","saeb","santra"]
# for fruit in Fruits:
#     print(fruit)

##2.
## n=int(input("Enter a series"))
# i=0
# while i<n:
#     print("*")
#     i+=1

##3.
## using for loop
#  for i in range(n):
#     print("##")

##4.
# for i in range(n):
#     if i==0:
#         print("**")
#     else:
#         print("***")

##5.
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

##6
# for i in range(1,5):
#     for j in range(1,i+1):
#         print( j,end=" ")
#     print()

# #7
# N = 5
# for i in range(1, N + 1 ):
#    for j in range(1, N-i+1):
#      print(" ", end="")
#    for j in range(1, i + 1 ):
#      print("*", end="")
#    print()

#8.prime using for loop and else
num=int(input("Enter a number: "))
if num>1:
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            print(f" {num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")