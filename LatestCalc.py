class OopCalc:
    def __init__(self, username):
        self.username = username

    def welcome_message(self):
        print(f"Welcome {self.username}! Feel free to use the calculator")

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            raise ValueError("Error: Cannot divide by zero") #Implemented error handling when dividing by 0

    def operations(self):
        try:
            print("Choose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            option = input("Enter the operation you want to carry out (1/2/3/4): ")

            num1 = float(input("Enter the First Number: "))
            num2 = float(input("Enter the Second Number: "))

            if option == '1':
                result = self.addition(num1, num2)
                print(f"The result for addition is {result}")

            elif option == '2':
                result = self.subtraction(num1, num2)
                print(f"The result for subtraction is {result}")

            elif option == '3':
                result = self.multiplication(num1, num2)
                print(f"The result for multiplication is {result}")

            elif option == '4':
                result = self.division(num1, num2)
                print(f"The result for division is {result}")

            else:
                print("Invalid Option")
        
        except ValueError as e: #Implemented error handling for invalid input e.g if i put a string datatype as my num1 or num2 
            print(e)

username = input("Enter your username: ")
calculator = OopCalc(username)
calculator.welcome_message()
calculator.operations()
