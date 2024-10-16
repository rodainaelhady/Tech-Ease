def check_password_strength(password):
    if len(password) < 8:
        return "weak"
    elif not any(char.isupper() for char in password):
        return "weak"
    elif not any(char.islower() for char in password):
        return "weak"
    elif not any(char.isdigit() for char in password):
        return "weak"
    elif not any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?`~' for char in password):
        return "weak"
    else:
        return "strong"
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password is", strength)