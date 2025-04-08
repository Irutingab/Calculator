


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
            print(f"All arguments must be numbers {args[1:]}")
            return None
        return func(*args, **kwargs)
    return wrapper


class Calculator:
    @logging_decorator
    @validation_decorator
    def add(self, *args):
        return sum(args)


    @logging_decorator
    @validation_decorator
    def subtract(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result


    @logging_decorator
    @validation_decorator
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result


    @logging_decorator
    @validation_decorator
    def divide(self, *args):
        result = args[0]
        for num in args[1:]:
            if num == 0:
                print("Division by zero is not applicable.")
            
                return None
            result /= num
        return result


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
                    print("Please choose a number between 1 and 5.")
            except ValueError:
                print("Invalid input")


    def get_numbers(self, operation=""):
        numbers = []
        while True:
            try:
                num = float(input(f"Enter a number to {operation} (or enter 'q' to finish): "))
                numbers.append(num)
            except ValueError:
                if len(numbers) > 0:
                    return numbers
                print("Inputs must be numbers")

                
    def run(self):
        while True:
            self.show_menu()
            choice = self.get_input()

            if choice == 1:  
                numbers = self.get_numbers("add")
                result = self.add(*numbers)
                print(f"Result: {result}")

            elif choice == 2:  
                numbers = self.get_numbers("subtract")
                result = self.subtract(*numbers)
                print(f"Result: {result}")

            elif choice == 3:  
                numbers = self.get_numbers("multiply")
                result = self.multiply(*numbers)
                print(f"Result: {result}")

            elif choice == 4:  
                numbers = self.get_numbers("divide")
                result = self.divide(*numbers)
                print(f"Result: {result}")

            elif choice == 5:  
                print("Exiting the calculator")
                break
            
            
def main():
    manager = Calculator()
    manager.run()
if __name__ == "__main__":
    main()