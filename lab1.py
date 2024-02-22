#!/usr/bin/python 3

from datetime import datetime, timedelta

# Obtain the present date
now = datetime.now()

# Prompt the user for their date of birth
print("Please provide your date of birth (YYYY-MM-DD): ")
dob = input()
while True:
    try:
        birthday = datetime.strptime(dob, "%Y-%m-%d")
        timeDifference = now - birthday
        age_in_years = timeDifference.days // 365
        break
    except(ValueError):
        birthday = input("Please provide your date of birth in the respected format (YYYY-MM-DD): ")


print(f"You're {age_in_years} years old!")


