import random
import string

def generate_password(length, chars):
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator\n")

    length = int(input("Enter password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    special_chars = '!@#$%^&*()-_+=<>?'

    chars = lowercase_chars
    if include_uppercase:
        chars += uppercase_chars
    if include_numbers:
        chars += number_chars
    if include_special:
        chars += special_chars

    password = generate_password(length, chars)

    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
