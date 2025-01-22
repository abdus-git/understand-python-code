p=float(input("Enter a principal value"))
r=float(input("Enter a rate value"))
t=float(input("Enter a time"))

SI=p*r*t/100
Amount=p*(1+r/100)**t
CI=Amount-p

print("The simple interest is",SI)
print("The amount of interest is",Amount)
print("The  compound interest is",CI)