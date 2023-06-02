def is_safe_password(password) -> bool:
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # If all conditions are satisfied, return True
    return True


if __name__ == "__main__":
    # Read the password from input
    password = input()

    # Check if the password is safe
    safe = is_safe_password(password)

    # Print the result
    print(str(safe).lower())
