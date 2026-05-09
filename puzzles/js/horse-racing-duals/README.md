# Horse Racing Duals

In this code, we first read the number of horses (N) from the input. Then, we iterate N times and read the strength of each horse, storing them in an array called strengths.

Next, we sort the strengths array in ascending order. Sorting the array allows us to find the minimum difference between adjacent strengths more easily.

We then initialize the minDiff variable with Infinity as a starting point for the minimum difference.

Next, we iterate through the sorted strengths array from the second element to the last, calculating the difference between each strength and its previous strength. If the calculated difference is smaller than the current minimum difference (minDiff), we update minDiff to the new smaller value.

Finally, we output the minDiff as the result.

You can run this code and test it with different inputs to see the output.
