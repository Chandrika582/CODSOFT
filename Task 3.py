import secrets
import string

def generate_password(length, use_uppercase, use_digits, use_specials):
    """Generate a secure password based on user preferences."""
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# User Input
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate and display password
    password = generate_password(length, use_uppercase, use_digits, use_specials)
    print("\nGenerated Password:", password)

except ValueError as e:
    print(f"Input Error: {e}")
