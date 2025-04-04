import datetime

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        all_args = ", ".join(map(str, args[1:]))  
        if kwargs:
            all_args += ", " + ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"{timestamp} - Calling {func.__name__} with arguments: {all_args}")
        try:
            result = func(*args, **kwargs)
            print(f"{timestamp} - {func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"{timestamp} - {func.__name__} raised an exception: {e}")
            raise  
    return wrapper

def validation_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args[1:]:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argument '{arg}' to {func.__name__} must be a number.")
        for val in kwargs.values():
            if not isinstance(val, (int, float)):
                raise TypeError(f"Argument '{val}' to {func.__name__} must be a number.")
        return func(*args, **kwargs)
    return wrapper

class Calculator:

    @logging_decorator
    @validation_decorator
    def add(self, a: float, b: float) -> float:
        """Adds two numbers."""
        return a + b

    @logging_decorator
    @validation_decorator
    def subtract(self, a: float, b: float) -> float:
        """Subtracts two numbers."""
        return a - b

    @logging_decorator
    @validation_decorator
    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers."""
        return a * b

    @logging_decorator
    @validation_decorator
    def divide(self, a: float, b: float) -> float:
        """Divides two numbers."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

# Example usage
calc = Calculator()
try:
    print(calc.add(5, 3))
    print(calc.subtract(10, b=2))
    print(calc.multiply(a=4, b=6))
    print(calc.divide(8, 0))
    print(calc.add(5, "hello"))
except TypeError as e:
    print(f"Type error: {e}")
except ZeroDivisionError as e:
    print(f"Division error: {e}")