# Horse Racing Duals

You have a list of N horses, each with a strength value, represented by an integer. You need to find the minimum difference in strength between two horses out of all possible pairs of horses. In other words, you need to find the two horses with the closest strength values.

For example, given the following list of horses with their corresponding strength values:

```
5 8 9 14 21
```

The minimum difference in strength between two horses is 1, which is the difference between 8 and 9.

The input for the problem consists of two lines. The first line contains an integer N, the number of horses. The second line contains N space-separated integers, representing the strength values of the N horses.

The output should be a single integer, the minimum difference in strength between two horses.

The solution to this problem involves sorting the list of horses in ascending order, and then computing the difference between adjacent horses in the sorted list. The minimum difference is the smallest of these computed differences.

## Code Example

```python
N = int(input())  # Read the number of horses

strengths = []  # Create an empty list for strengths

# Read the strengths of each horse and append them to the list
for _ in range(N):
    strength = int(input())
    strengths.append(strength)

strengths.sort()  # Sort the list of strengths

min_diff = float('inf')  # Initialize min_diff with a large value

# Find the minimum difference between strengths
for i in range(1, N):
    diff = strengths[i] - strengths[i-1]
    if diff < min_diff:
        min_diff = diff

print(min_diff)  # Print the minimum difference as the output

```

## Edge Cases

When considering the algorithm for comparing horses' strengths, several scenarios need addressing. Firstly, account for an empty input list, ensuring the algorithm handles the absence of horses gracefully. Secondly, handle the case where only one horse is in the list with care. Thirdly, address scenarios with duplicate strength values, testing the algorithm's response to ties or identical strengths. Additionally, assess whether negative strength values are permitted and how they're managed in sorting and computation. Evaluate the algorithm's efficiency and scalability with significantly large input sizes and test its robustness with extreme values, checking for correct handling of overflow or underflow cases. Validate the sorting step by generating randomized input where strengths are initially unsorted. Furthermore, consider scenarios where all strengths are equal to ensure the algorithm doesn't falter in cases of uniformity. Lastly, test the algorithm's ability to identify the minimum difference despite alternating strength values between high and low, ensuring it handles varied patterns effectively.
