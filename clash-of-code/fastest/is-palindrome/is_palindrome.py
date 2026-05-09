def is_palindrome(n):
    binary = bin(n)[2:]  # Convert n to binary representation without '0b' prefix
    if binary == binary[::-1]:  # Check if binary representation is a palindrome
        if len(binary) % 2 == 0:  # Check if length of binary representation is even
            return "YES"
        else:
            return "yes"
    else:
        return "no"


if __name__ == "__main__":
    # Test cases
    assert is_palindrome(4) == "no"
    assert is_palindrome(9) == "YES"
    assert is_palindrome(10) == "no"
    assert is_palindrome(255) == "YES"
    assert is_palindrome(85) == "yes"
    assert is_palindrome(135) == "no"
