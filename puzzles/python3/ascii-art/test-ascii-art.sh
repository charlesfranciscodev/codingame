#!/bin/bash

# Call the Python script and capture the output
output=$(python3 puzzles/python3/ascii-art/ascii_art.py < puzzles/python3/ascii-art/input.txt)

# Expected output
expected_output=" ##  #  ##  ### ###  ##  #  # # ### 
#   # # # #  #  # # #   # # ### #   
#   # # # #  #  # # # # ### ### ##  
#   # # # #  #  # # # # # # # # #   
 ##  #  ##  ### # #  ## # # # # ### "

# Compare the output with the expected output
if [[ "$output" == "$expected_output" ]]; then
  printf "Integration test passed!\n"
else
  printf "Integration test failed.\nExpected:\n$expected_output\nGot:\n$output\n"
fi
