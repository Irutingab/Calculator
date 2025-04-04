



def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args[1:]}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def validation_decorator(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args[1:]):
            print(f"Error: All arguments must be met {args[1:]}")
            return None
        return func(*args, **kwargs)
    return wrapper

class Calculator:
    @logging_decorator
    @validation_decorator
    def add(self, a, b):
        return a + b

    @logging_decorator
    @validation_decorator
    def subtract(self, a, b):
        return a - b

    @logging_decorator
    @validation_decorator
    def multiply(self, a, b):
        return a * b

    @logging_decorator
    @validation_decorator
    def divide(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return a / b

    def show_menu(self):
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def get_input(self):
        while True:
            try:
                choice = int(input("\nEnter the number of the operation you want to perform (1-5): "))
                if choice in [1, 2, 3, 4, 5]:
                    return choice
                else:
                    print("Invalid choice. Please choose a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_numbers(self):
        while True:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                return a, b
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_input()

            if choice == 1:  
                a, b = self.get_numbers()
                print(f"Result: {self.add(a, b)}")

            elif choice == 2:  
                a, b = self.get_numbers()
                print(f"Result: {self.subtract(a, b)}")

            elif choice == 3:  
                a, b = self.get_numbers()
                print(f"Result: {self.multiply(a, b)}")

            elif choice == 4:  
                a, b = self.get_numbers()
                print(f"Result: {self.divide(a, b)}")

            elif choice == 5:  
                print("Exiting the calculator")
                break



