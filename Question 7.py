# Define a custom exception class called NegativeNumberError that inherits from the
# built-in Exception class. Write a function check_positive that raises this exception if
# a given number is negative.
# Demonstrate the use of this function in a try block.

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