def Celisus(Celisus1):
    return(Celisus1 * 9/5) + 32
def Fahrenheit(Fahrenheit1):
    return(Fahrenheit1 - 32) * 5/9
choice = input("For convert Celisus to Fahrenheit enter C or F for Fahrenheit to Celisus : ")
if choice == 'C':
    Celisus1 = float(input("Enter the celisus Temp : "))
    print(f"{Celisus1} C is equal to {Celisus(Celisus1) : .2f} F")
elif choice == 'F':
    Fahrenheit1=float(input("Enter the fahrenheit Temp : "))
    print(f"{Fahrenheit1} F is equal to {Fahrenheit(Fahrenheit1) : 2f} C")
else:
    print("Invalid choice. please select either C or F")