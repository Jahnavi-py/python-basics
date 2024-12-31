#Write a program to calculate the compound interest given principal, rate, and time.
principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest : "))
time = float(input("Enter the years to pay loan"))
compound_interest = principal * (1 + rate /100) ** time
print(compound_interest)