import random
import string

def generate_password(length=10):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
password = generate_password()
print("Random Password:", password)