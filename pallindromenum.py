#check pallindrome or not
num=int(input("Enter a number: "))
temp=num
rev=0
while(num!=0):
    digit=num%10
    rev=(rev*10)+digit
    num=num//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("The number is not palindrome")