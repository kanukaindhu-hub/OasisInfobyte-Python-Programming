import random
import string

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nSelect character types:")
        upper = input("Include Uppercase letters? (y/n): ").lower() == 'y'
        lower = input("Include Lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include Numbers? (y/n): ").lower() == 'y'
        symbols = input("Include Symbols? (y/n): ").lower() == 'y'

        selected = sum([upper, lower, digits, symbols])

        if selected < 2:
            print("Please select at least TWO character types.")
            continue

        chars = ""
        password = []

        if upper:
            chars += string.ascii_uppercase
            password.append(random.choice(string.ascii_uppercase))

        if lower:
            chars += string.ascii_lowercase
            password.append(random.choice(string.ascii_lowercase))

        if digits:
            chars += string.digits
            password.append(random.choice(string.digits))

        if symbols:
            chars += string.punctuation
            password.append(random.choice(string.punctuation))

        while len(password) < length:
            password.append(random.choice(chars))

        random.shuffle(password)

        print("\nGenerated Password:")
        print("".join(password))

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("Thank you!")
            break

    except ValueError:
        print("Please enter a valid number.")