num1 =int(input("Enter number"))
num2 = int(input("Enter number"))
operator =input("Enter operator :{+,-,*,/,%}")

if operator == "+":
    print("Addition: ",num1+num2)
elif operator == "-":
    print("Subtraction: ",num1-num2)
elif operator == "*":
    print("Multiplication: ",num1*num2)
elif operator == "/":
    print("Division: ",num1/num2)
elif operator == "%":
    print("Modulus: ",num1%num2)

else:
    print("END OF CODE")

