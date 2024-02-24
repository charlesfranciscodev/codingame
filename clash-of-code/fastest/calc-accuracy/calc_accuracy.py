def calculate_accuracy(key: str, submission: str) -> float:
    if len(key) == 0 and len(submission) == 0:
        return 1.0
    else:
        matching_chars = sum(a == b for a, b in zip(key, submission))
        return matching_chars / len(key)


if __name__ == "__main__":
    key_phrase = input().lower()  # Read the key phrase
    num_submissions = int(input()).lower()  # Read the number of submissions

    for _ in range(num_submissions):
        submission = input()  # Read each submission
        accuracy = calculate_accuracy(key_phrase, submission)

        if accuracy >= 0.9:  # Check if the accuracy meets the passing criteria
            print("pass")
        else:
            print("fail")
