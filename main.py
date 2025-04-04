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
            print(f"Error: All arguments must be numbers. Received {args[1:]}")
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
