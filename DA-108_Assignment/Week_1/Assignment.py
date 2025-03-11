from datetime import datetime

# Get the current date
today = datetime.today()

# Ask for user's birth year, month, and day
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Calculate age
age = today.year - birth_year
if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
    age -= 1  # If birthday hasn't happened yet this year, subtract 1

# Calculate next birthday
next_birthday = datetime(today.year, birth_month, birth_day)
if today > next_birthday:
    next_birthday = datetime(today.year + 1, birth_month, birth_day)

# Calculate days until next birthday
days_until_birthday = (next_birthday - today).days

# Print results
print(f"Your age: {age} years")
print(f"Days until your next birthday: {days_until_birthday} days")
