#!/usr/bin/python 3

from datetime import datetime, timedelta

# Obtain the present date
now = datetime.now()

# Prompt the user for their date of birth
print("Please provide your date of birth (YYYY-MM-DD): ")
dob = input()

# Convert the user's input into datetime 
birthday = datetime.strptime(dob, "%Y-%m-%d")

# Calculate the difference between the present and birthday
timeDifference = now - birthday

# Determine the person's age via years
age_in_years = timeDifference.days // 365

print(f"You're {age_in_years} years old!")
