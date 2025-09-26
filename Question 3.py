while True:
    user_input = input("Please enter a number: ")
    try:
        number = float(user_input)  # You can use int(user_input) if you want only integers
        print(f"Great! You entered the number: {number}")
        break
    except ValueError:
        print("Oops! That wasn't a valid number. Please try again.")
