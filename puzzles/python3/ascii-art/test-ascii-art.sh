#!/bin/bash

# Call the Python script and capture the output
output=$(python3 puzzles/python3/ascii-art/ascii_art.py < puzzles/python3/ascii-art/input.txt)

# Expected output
expected_output="# # ### ### # # ### ### ### ### ### 
###   # # # # #   #  #   #    # # # 
###  ## # # ###  ##  #   #   ## # # 
# #     # # # #      #   #      # # 
# #  #  # # # #  #   #   #   #  # # "

# Compare the output with the expected output
if [[ "$output" == "$expected_output" ]]; then
  echo "Integration test passed!"
else
  echo "Integration test failed. Expected: $expected_output. Got: $output"
fi
