#George Githigi Ngugi - SCT211-0460/2022

import datetime
username = input("Enter your name: ")
print(f"Welcome {username}! Feel free to use this age calculator.")

year_of_birth = int(input("Enter your year of birth: "))
month_of_birth = int(input("Enter your month of birth (1-12): "))
day_of_birth = int(input("Enter your day of birth: "))

# Get the current date
current_date = datetime.date.today()

# Calculate the age
birth_date = datetime.date(year_of_birth, month_of_birth, day_of_birth)
age = current_date - birth_date

# Extract years, months, and days from the age difference
years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30
days = remaining_days % 30

print(f"You are {years} years, {months} months, and {days} days old.")
