principal = float(input("Enter principal amount:"))
rate = float(input("Enter the interset rate:"))
time = int(input("enter the time in years:"))
compound_interset = principal *(1 + rate/100) * time
print("Compund Interset:", compound_interset)
