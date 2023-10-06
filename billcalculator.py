#George Githigi Ngugi - SCT211-0460/2022

# Get user input
total_bill = float(input("Enter the total bill amount: $"))
print("Select tip percentage:")
print("1. 10")
print("2. 12")
print("3. 15")
tip_percentage = int(input("Enter the tip percentage: "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Calculate the total amount to be paid, including the tip
total_amount = total_bill + tip_amount

# Calculate the amount each person should pay
amount_per_person = total_amount / num_people

# Round the result to two decimal places
amount_per_person = round(amount_per_person, 2)

# Display the result
print(f"Each person should pay: ${amount_per_person}")
