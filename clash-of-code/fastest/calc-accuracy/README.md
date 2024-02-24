# Key Phrase Accuracy Evaluator

This Python script evaluates the accuracy of submissions against a key phrase. It calculates the accuracy based on the number of matching characters between the key phrase and the submission.

## Function: `calculate_accuracy(key, submission) -> float`

This function calculates the accuracy of a submission compared to a key phrase.

- **Parameters**:
    - `key` (str): The key phrase against which the submission is compared.
    - `submission` (str): The submission to evaluate.

- **Returns**:
    - `accuracy` (float): The accuracy of the submission as a floating-point number between 0.0 and 1.0.

## Note

- The accuracy calculation is case-sensitive.
- Empty key phrases and submissions result in an accuracy of 1.0.
- The passing criteria for accuracy is set to 90% (0.9).
