# Ask question from users
name = input("What's your name? ")

# Removed extra spaces from the users input
name = name.strip()

# Capitalize the WORD FIRST LETTER from recived the users
# name = name.capitalize()

# Capitalize the users name and title
name = name.title()

# Using the f function to print one line and attached the variable
print(f"hello, {name}")


# using the all function in one line
name = input("whta's your name? ").strip().title()
print(f"hello, {name}")