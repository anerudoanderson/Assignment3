# Define the custom exception
class NegativeNumberError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative number detected: {value}")
        self.value = value

# Function that checks if a number is positive
def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"{number} is a positive number.")

# Demonstration using try-except
try:
    num = -7  # You can change this to test other values
    check_positive(num)
except NegativeNumberError as e:
    print("Caught an exception:", e)
