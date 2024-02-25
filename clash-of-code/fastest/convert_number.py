def decimal_to_binary(decimal):
    return bin(decimal)[2:]


def binary_to_decimal(binary):
    return int(binary, 2)


def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:].upper()


def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)


def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)


def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)


# Function to convert numbers based on input and output types
def convert_number(input_type, output_type, number):
    if input_type == "bin" and output_type == "dec":
        return binary_to_decimal(number)
    elif input_type == "bin" and output_type == "hex":
        return binary_to_hexadecimal(number)
    elif input_type == "dec" and output_type == "bin":
        return decimal_to_binary(int(number))
    elif input_type == "dec" and output_type == "hex":
        return decimal_to_hexadecimal(int(number))
    elif input_type == "hex" and output_type == "bin":
        return hexadecimal_to_binary(number)
    elif input_type == "hex" and output_type == "dec":
        return hexadecimal_to_decimal(number)
    else:
        return None


# Main program
n = int(input())

for _ in range(n):
    input_type, output_type, number = input().split()
    converted_number = convert_number(input_type, output_type, number)
    print(converted_number)
