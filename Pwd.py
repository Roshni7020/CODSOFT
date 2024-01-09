#Importing Random And string
import random
import string

#Introducing Characters we will use to generate password
def generate_password(length=12, uppercase=True, digits=True, special_chars=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    if not characters:
        print("Error: No character set selected. Please enable at least one option.")
        return None

#Generating password within Length 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Introducing loop
def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid positive integer.")

    uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    digits = input("Include digits? (yes/no): ").lower() == "yes"
    special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, uppercase, digits, special_chars)

    if password:
        print(f"\nGenerated Password: {password}")

main()