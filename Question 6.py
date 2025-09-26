def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both inputs must be numbers.")

# Example usage
print(divide_numbers(20, 4))      # Outputs: 5.0
print(divide_numbers(30, 0))      # Outputs: Error message
print(divide_numbers("20", 4))    # Outputs: Error message
