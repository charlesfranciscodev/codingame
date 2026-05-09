def validate_cryptichip_number(number):
    number = number.replace(" ", "")  # Remove spaces
    if len(number) != 13:
        return False

    total_sum = sum(int(number[i]) * (i + 1) for i in range(12))
    last_digit = total_sum % 10
    return int(number[-1]) == last_digit


if __name__ == "__main__":
    n = int(input())  # Number of Cryptichip numbers to validate

    for _ in range(n):
        cryptichip_number = input().strip()
        if validate_cryptichip_number(cryptichip_number):
            print("Valid")
        else:
            print("Invalid")
