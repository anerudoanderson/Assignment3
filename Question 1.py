# 1. Write a Python function named classify_number that takes an integer as input and
# returns:
# "Positive" if the number is greater than zero.
# "Negative" if the number is less than zero.
# "Zero" if the number is zero.
# Use a while loop to repeatedly prompt the user for a number until they enter a valid integer.

def classify_number():
    while True:
        user_input = input("Enter an integer (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            number = int(user_input)
            if number > 0:
                print("Positive")
            elif number < 0:
                print("Negative")
            else:
                print("Zero")
        except ValueError:
            print("That's not a valid integer. Please try again.")

classify_number()