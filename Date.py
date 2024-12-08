from datetime import datetime, date, timedelta
date_str = input("Enter a date (YYYY-MM-DD): ")
given_date = datetime.strptime(date_str, "%Y-%m-%d")
next_day = given_date + timedelta(days=1)
print("The next day is:", next_day.strftime("%Y-%m-%d"))