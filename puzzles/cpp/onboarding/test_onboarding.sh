#!/bin/bash

# Test case 1
expected_output1="Orc"

# Test case 2
expected_output2="Dragon"

# Function to compare expected and actual outputs
compare_output() {
    expected_output=$1
    actual_output=$2
    if [[ "$expected_output" == "$actual_output" ]]; then
        echo "Test passed!"
    else
        echo "Test failed!"
        echo "Expected output: $expected_output"
        echo "Actual output: $actual_output"
    fi
}

# Compare the outputs
compare_output "$expected_output1" "$(./program < puzzles/cpp/onboarding/output1.txt)"
compare_output "$expected_output2" "$(./program < puzzles/cpp/onboarding/output2.txt)"
