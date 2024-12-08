print("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
month = input("Enter the month : ")
if month == "Feb":
        print ("The number of days are : 28/29 days")
elif  month in ("Jan", "Mar", "May", "July", "Aug","Oct","Dec"):
        print("The Number of days are : 31 days")
elif month in ( "Apr", "June", "Sept", "Nov"):
    print("The number of days are : 30 days")
else:
    print("Invalid month")
