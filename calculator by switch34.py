#WAP to Simulate Arithmetic Calculator using switch

n1= float(input("Enter a number: "))
n2= float(input("Enter another number: "))
n=int((input("Enter user's choice (+,-,*,/,even or odd): ")))

match n:
    case 1:
        print("Sum",n1+n2)
    case 2:
        print("Product",n1*n2)
    case 3:
        print("Division",n1/n2)
    case 4:
        print("Difference",n1-n2)
    case 5:
        if n1%2==0 :
            print(n1,"is an even number")
        else:
            print(n1,"is an odd number")
    case _:
        print("Invalid choice")
