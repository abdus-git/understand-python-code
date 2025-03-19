#WAP for electricity bill first100 unit $0.5/unit 2nd 100unit $0.75/unit above 200 $1/unit

units=int(input("Enter the units: "))
if units<=100:
    amount=units*0.5
    print("Electricity bill in $",amount)
elif 100<units<200:
    amount=(100*0.5) + ((units-100)*0.75)
    print("Electricity bill in $",amount)
else:
    amount=(100*0.5) + (100*0.75) +((units-200)*1)
    print("Electricity bill in $",amount)
