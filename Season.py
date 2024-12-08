'''read two integers month and day and print season
month = input("Enter the month: ").capitalize()
day = int(input("Enter the day: "))
if month in ("Jan", "Feb", "March"):
    season = "Spring"
elif month in ("April", "May", "June"):
    season = "Summer"
elif month in ("July", "August", "September"):
    season = "Fall Autumn"
else:
    season = "Winter"
if (month == "March" and day >= 19):
    season = "Spring"
elif (month == "June" and day >= 20):
    season = "Summer"
elif (month == "September" and day >=22):
    season = "Fall Autumn"
elif (month == "December" and day >=21):
    season = "Winter"
print("Season is",season)'''
month = input("Enter the month: ").capitalize()
day = int(input("Enter the day: "))
if month in ("January", "February"):
    season = "Winter"
elif month == "March":
    season = "Winter" if day < 20 else "Spring"
elif month in ("April", "May"):
    season = "Spring"
elif month == "June":
    season = "Spring" if day < 21 else "Summer"
elif month in ("July", "August"):
    season = "Summer"
elif month == "September":
    season = "Summer" if day < 22 else "Fall Autumn"
elif month in ("October", "November"):
    season = "Fall Autumn"
elif month == "December":
    season = "Fall Autumn" if day < 21 else "Winter"
else:
    season = "Invalid month"
if season != "Invalid month":
    print("Season is", season)
else:
    print("Invalid month entered. Please try again.")