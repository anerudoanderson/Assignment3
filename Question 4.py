# Create a Python script that writes a list of names to a file called names.txt. Each
# name should be on a new line. Then, read the file and print each name to the
# console. Use the with statement to handle file operations and ensure the file is
# properly closed.

# List of names to write to the file
names = ["Nomagugu", "Nathan", "Munashe", "Audry", "Kudzai"]

# Write names to 'names.txt', each on a new line
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read and print each name from the file
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character