import re

# Create sample input file
sample_text = """
support@gmail.com
info@yahoo.com
test123@outlook.com
"""

with open("input.txt", "w") as file:
    file.write(sample_text)

# Read file
with open("input.txt", "r") as file:
    text = file.read()

# Extract emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Extracted Emails:")
for email in emails:
    print(email)