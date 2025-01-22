#To check ARMSTRONG NUMBER OR NOT(153=1^3+5^3+3^3)

num=int(input("enter a number"))
temp =num
sum=0
while num!=0:
    div =num%10
    sum =sum+(div*div*div)
    num =num//10
if temp == sum:
        print("number is armstrong ")
else:
        print("number is not armstrong")