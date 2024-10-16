import random
import string
def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = ''.join(random.sample(all_characters, length))
    return password
password = generate_password()
print("Generated Password:", password)