from validate_crypt_number import validate_cryptichip_number


def test_validate_cryptichip_number():
    # Valid Cryptichip numbers
    assert validate_cryptichip_number("3380078466704") is True
    assert validate_cryptichip_number("1930765426573") is True
    assert validate_cryptichip_number("9328470699181") is True
    assert validate_cryptichip_number("5534513211235") is True

    # Invalid Cryptichip numbers
    assert validate_cryptichip_number("1234567890123") is False  # Last digit should be 5, not 3
    assert validate_cryptichip_number("4567890123456") is False  # Last digit should be 0, not 6
    assert validate_cryptichip_number("1111111111111") is False  # Last digit should be 0, not 1
    assert validate_cryptichip_number("123456789012") is False   # Length is not 13

    print("All tests passed!")


if __name__ == "__main__":
    test_validate_cryptichip_number()
