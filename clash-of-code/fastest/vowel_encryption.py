def encrypt_message(s):
    # Initialize variables to store the sum and count of lowercase vowels
    vowel_sum = 0
    vowel_count = 0

    # Define the set of lowercase vowels
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    # Iterate through the characters in the input string
    for char in s:
        # Check if the character is a lowercase vowel
        if char in vowels:
            # Add the ASCII code of the vowel to the sum
            vowel_sum += ord(char)
            # Increment the count of lowercase vowels
            vowel_count += 1

    # Calculate the final product
    final_product = vowel_sum * vowel_count

    return final_product

# Read the input string from the user
s = input()

# Calculate and print the final product
result = encrypt_message(s)
print(result)
