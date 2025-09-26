# What is an API? Explain how to make a GET request to an API using the requests
# library in Python.
# · Explain how to connect to a SQLite database using Python. Describe the
# steps involved and the purpose of each step.

# An API (Application Programming Interface) is a set of rules that allows software applications to communicate with each other. Think of it as a waiter in a restaurant—you tell it what you want (a request), and it brings back what the kitchen (server) provides (a response).
# APIs are commonly used to:
# - Access data from web services (e.g., weather, stock prices, social media)
# - Interact with databases or cloud platforms
# - Automate tasks across different applications
#
# 🔗 Making a GET Request with requests in Python

import requests

# Define the API endpoint
url = "https://api.example.com/data"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    data = response.json()       # Parse JSON response
    print("Received data:", data)
except requests.exceptions.RequestException as e:
    print("API request failed:", e)



# Connecting to a SQLite Database in Python
# SQLite is a lightweight, file-based database that’s great for small projects. Python has built-in support via the sqlite3 module.

import sqlite3

try:
    # Step 1: Connect to the database (creates file if it doesn't exist)
    conn = sqlite3.connect("my_database.db")

    # Step 2: Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Step 3: Execute SQL commands (e.g., create table)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)

    # Step 4: Commit changes to save them
    conn.commit()

    # Step 5: Close the connection when done
    conn.close()

except sqlite3.Error as e:
    print("SQLite error:", e)