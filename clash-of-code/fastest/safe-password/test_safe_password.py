from safe_password import is_safe_password


def test_is_safe_password():
    # Test a password with length less than 8
    assert is_safe_password("short") is False

    # Test a password with length equal to 8
    assert is_safe_password("secure12") is True

    # Test a password with length greater than 8
    assert is_safe_password("longpassword123") is True

    # Test a password without any digits
    assert is_safe_password("password") is False

    # Test a password with at least one digit
    assert is_safe_password("password1") is True

    # Test a password without any lowercase letters
    assert is_safe_password("PASSWORD1") is False

    # Test a password with at least one lowercase letter
    assert is_safe_password("Password1") is True

    # Test a password without any uppercase letters
    assert is_safe_password("password1") is False

    # Test a password with at least one uppercase letter
    assert is_safe_password("Password1") is True

    # Test a password that meets all conditions
    assert is_safe_password("SecurePass123") is True

    # Test a password that does not meet any conditions
    assert is_safe_password("123") is False

    print("All tests pass")


if __name__ == "__main__":
    test_is_safe_password()
