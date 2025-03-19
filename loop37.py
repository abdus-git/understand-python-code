#print name by loop
# name = str(input("Enter your name:"))
# for i in range(5):
#     print(name)

# for j in range(10,0,-2):
#     print(name)

#sum of 10's digit between 20 and 100 by
# 1.WHILE LOOP:
i=100
sum=0
while i>10:
    sum = sum + i
    i-=10
print("The  ",sum)

# 2. FOR LOOP
sum=0
for i in range(20,101):
    if i%10==0:
        sum=sum+i
print("The sum of 10's digit between 20 and 100: ",sum)
