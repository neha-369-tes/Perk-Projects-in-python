import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    char_sets = []
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)  # A-Z
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)  # a-z
    if use_numbers:
        char_sets.append(string.digits)  # 0-9
    if use_symbols:
        char_sets.append(string.punctuation)  # Special characters

    if not char_sets:
        print("Error: You must select at least one character type!")
        return None

    if length < len(char_sets):
        print(f"Error: Password length must be at least {len(char_sets)} to include all selected character types.")
        return None

    # Ensure at least one character from each selected set
    password = [random.choice(cs) for cs in char_sets]

    # Fill the rest randomly
    all_chars = "".join(char_sets)
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return "".join(password)

# User Input
print("🔐 Random Password Generator 🔐")

try:
    length = int(input("Enter password length (minimum 4): "))
    if length < 4:
        print("Error: Password length must be at least 4!")
        exit()
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

# Generate and Display Password
password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)

if password:
    print("\n✅ Generated Password:", password)
