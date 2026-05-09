#!/bin/bash

read -p "Number of horses: " n

# Read the strengths into an array
for ((i=0; i<n; i++)); do
    read -p "Strength of horse $((i+1)): " strengths[$i]
done

# Sort the strengths in ascending order
sorted=($(printf '%s\n' "${strengths[@]}" | sort -n))

# Initialize the minimum difference with a large value
min_diff=10000000

# Find the minimum difference between adjacent strengths
for ((i=1; i<n; i++)); do
    diff=$((sorted[i] - sorted[i-1]))
    if (( diff < min_diff )); then
        min_diff=$diff
    fi
done

echo "$min_diff"
