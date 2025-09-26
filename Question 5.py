# Sample list of temperatures in Celsius
celsius_temps = [10, 25, 35, 45, 53, 60]

# Convert to Fahrenheit using map and a lambda function
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

# Print the converted list
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)
