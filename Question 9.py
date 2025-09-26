# Write a program that:
# I. Uses regular expressions to extract all email addresses from a given text.
# II. Uses regular expressions to validate a date in the format &quot;YYYY-MM-DD&quot;.
# III. Uses regular expressions to replace all occurrences of a word with another word in
# a string.
# IV. Use regular expressions to split a string by all non-alphanumeric characters.

import re

# I. Extract all email addresses from a given text
text = "Contact us at support@example.com, sales@company.org, or admin123@mail.co.uk."
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Extracted Emails:", emails)

# II. Validate a date in the format "YYYY-MM-DD"
def validate_date(date_str):
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    if re.match(pattern, date_str):
        print(f"Valid date: {date_str}")
    else:
        print(f"Invalid date: {date_str}")

validate_date("2025-09-14")  # Valid
validate_date("2025-13-01")  # Invalid

# III. Replace all occurrences of a word with another word in a string
original_text = "The weather is sunny. Sunny days are the best."
replaced_text = re.sub(r'\bsunny\b', 'cloudy', original_text, flags=re.IGNORECASE)
print("Replaced Text:", replaced_text)

# IV. Split a string by all non-alphanumeric characters
messy_string = "Hello! How's everything going? Great, I hope."
split_words = re.split(r'\W+', messy_string)
print("Split Words:", [word for word in split_words if word])  # Remove empty strings