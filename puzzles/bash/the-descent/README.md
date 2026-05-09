# The Descent

## Solution

```bash
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
```

The script enters an infinite loop to continuously read the heights of the mountains and determine the index of the highest one. It keeps track of the maximum height and its corresponding index as it iterates through the input. Finally, it outputs the index of the highest mountain.

Please note that this script assumes the input is provided correctly, following the specified format.
