#George Githigi Ngugi - SCT211-0460/2022

username = input("Enter your name: ")
print(f"Welcome {username}! Feel free to use this calculator.")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the operation number (1/2/3/4): ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == "1":
   result = num1 + num2
   print("The addition of the two numbers is:", result)
elif choice == "2":
   result = num1 - num2
   print("The subtraction of the two numbers is:", result)
elif choice == "3":
   result = num1 * num2
   print("The multiplication of the two numbers is:", result)
elif choice == "4":
    result = num1 / num2
    print("The division of the two numbers is:", result)
else:
   print("Invalid Input")
