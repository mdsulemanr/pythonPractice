import string
import secrets

def generate_complex_password(length: int = 12):
    """
    Generate a secure, complex password of given length.
    Ensures at least one uppercase, lowercase, digit, and special character.
    """

    if length < 12:
        raise ValueError("Password length must be at least 12 characters")

    # Character groups
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    specials = "!@#$%^&*()-_=+[]{};:,.?/"

    # Combine all character groups
    all_chars = uppercase + lowercase + digits + specials

    # Ensure at least one character from each group
    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(specials),
    ]

    # Fill the rest randomly from all characters
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))

    # Secure shuffle (Fisher–Yates)
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    # Convert list to string
    password = ''.join(password_chars)
    return password


# Example usage
if __name__ == "__main__":
    print("Generated Password:", generate_complex_password())
