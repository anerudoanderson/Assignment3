# Write a program that handles user input for a number. Use a try block to catch any
# ValueError exceptions that may occur if the user inputs an invalid number. Print an
# error message and prompt the user to enter a valid number again.

while True:
    user_input = input("Please enter a number: ")
    try:
        number = float(user_input)  # You can use int(user_input) if you want only integers
        print(f"Great! You entered the number: {number}")
        break
    except ValueError:
        print("Oops! That wasn't a valid number. Please try again.")