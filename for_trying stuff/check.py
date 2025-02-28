import datetime

def birthday_countdown():
    """Calculates age and days until next birthday (beginner-friendly)."""

    print("Let's calculate your age and birthday countdown!")

    # 1. Get birthdate input (easy version):
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    birth_date = datetime.date(birth_year, birth_month, birth_day)  # Create date object

    # 2. Get today's date:
    today = datetime.date.today()

    # 3. Calculate age (simplified):
    age = today.year - birth_date.year

    # Check if birthday has already passed this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1  # Adjust age if birthday hasn't happened yet

    print(f"You are {age} years old.")

    # 4. Determine next birthday:
    next_birthday = datetime.date(today.year, birth_date.month, birth_date.day)

    if next_birthday < today:  # If birthday is in the past
        next_birthday = datetime.date(today.year + 1, birth_date.month, birth_date.day)

    # 5. Calculate countdown:
    days_until_birthday = (next_birthday - today).days

    # 6. Display results (easy version):
    if days_until_birthday == 0:
        print("Wish you a Happy Birthday! from Sarthak ")
    elif days_until_birthday > 0:
        print(f"Your birthday is in {days_until_birthday} days.")
    else:
        print("Something went wrong with the calculation.")  # Basic error message


# Run the program:
birthday_countdown()