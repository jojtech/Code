#George Githigi Ngugi - SCT211-0460/2022
# Input from the users 
weight = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))

# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

# Define BMI categories
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
else:
    category = "Overweight"

# Display the result
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")

