import random

# Generate a list of 10 random integers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Calculate the average
average = sum(random_numbers) / len(random_numbers)

# Print the results
print("Random numbers:", random_numbers)
print("Average:", round(average, 2))  # Rounded to 2 decimal places
