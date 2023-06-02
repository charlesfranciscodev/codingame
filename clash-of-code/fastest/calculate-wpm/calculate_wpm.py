def calculate_words_per_minute(words, typed, time):
    # Calculate the number of characters typed
    characters_typed = len(typed)

    # Calculate the number of errors
    errors = sum([1 for i in range(len(typed)) if typed[i] != words[i]])

    # Calculate the number of words per minute
    words_per_minute = (characters_typed / 5 - errors) / (time / 60)

    # Round the result to the nearest integer
    words_per_minute = round(words_per_minute)

    return words_per_minute

# Read the input
words = input().strip()
typed = input().strip()
time = int(input().strip())

# Call the function and print the result
result = calculate_words_per_minute(words, typed, time)
print(result)
