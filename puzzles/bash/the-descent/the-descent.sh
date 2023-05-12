#!/bin/bash

while true; do
    max_height=0
    max_index=0
    
    # Read the heights of the mountains
    for ((i=0; i<8; i++)); do
        read mountainH
        
        # Check if the current mountain is taller than the previous tallest
        if ((mountainH > max_height)); then
            max_height=$mountainH
            max_index=$i
        fi
    done
    
    # Output the index of the highest mountain
    echo $max_index
done
