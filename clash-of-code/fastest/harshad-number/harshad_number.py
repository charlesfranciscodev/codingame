def is_harshad_number(n):
    # Calculate the sum of the digits of n
    digit_sum = sum(int(digit) for digit in str(n))

    # Check if n is divisible by digit_sum
    if n % digit_sum == 0:
        return True
    else:
        return False
