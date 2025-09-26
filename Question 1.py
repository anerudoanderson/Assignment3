# Question 1

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
