         #IF CONDITION
#age
# age=int(input("Enter your age:"))
# if(age >= 18):
#     print("Adult")
#
# #even or not
# num=int(input("Enter your number:"))
# if(num%2==0):
#     print("Even")
# if(num%2!=0):
#     print("Odd")
#
# #check positive number
# n=int(input("Enter your number:"))
# if(n>0):
#         print("Number is positive")
# if(n<0):
#     print("Number is negative")
# if(n==0):
#     print("Number is zero")
#
#     #IF ELSE COND
#     #age
# age=int(input("Enter your age:"))
# if age>=18:
#     print("You are eligible to vote")
# else :
#     print("You are not eligible to vote")
#     #even or odd
# num=int(input("Enter your number to check even or odd:"))
# if num%2==0:
#      print("Even")
# else :
#     print("Odd")
#
# #check +ve or-ve number
# n=int(input("Enter your number to check positive or negative:"))
# if n>0:
#     print("Number is positive")
# elif n<0:
#     print("Number is negative")
# else :
#     print("Number is zero")
#
# WAP to print you are eligible for vote if you are 18+  and citizen of India
age=int(input("Enter your age for vote eligibility:"))
country=input("Enter your country name:")
if age>=18:
    if country=="India":
        print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#WAP if perc>=85 grade"A" , per bw 80and 75 grade "B" grade "C" 70and 65 grade"D" 60 and 50 grade "E" 50 and 30
per=int(input("Enter your percentage "))
if per>=85:
    print("Grade:A")
elif 75<per<80:
    print("Grade:B")
elif 65<per<70:
    print("Grade:C")
elif 50<per<60:
    print("Grade:D")
elif 30<per<50:
    print("Grade:E")
else:
    print("Grade:F")