# List of names to write to the file
names = ["Sam", "Anerudo", "Anderson", "Zivai", "Thompson"]

# Write names to 'names.txt', each on a new line
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read and print each name from the file
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character
