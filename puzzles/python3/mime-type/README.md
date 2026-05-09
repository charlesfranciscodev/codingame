# MIME Type

## Description

The task involves creating a program to determine the MIME type of files based on their names. This involves associating file extensions with MIME types. The program reads an association table with N elements and a list of Q file names to be analyzed. For each file name, the program identifies the extension by finding the substring after the last dot character. If the extension is found in the association table (case insensitive), it prints the corresponding MIME type. If the MIME type cannot be determined or the file has no extension, it outputs UNKNOWN. The program takes the number of elements in the table, the number of file names, the extension-MIME associations, and the file names as input, and outputs the corresponding MIME types or UNKNOWN.

## Solution Overview

To solve this problem, we need to map file extensions to their respective MIME types, and then analyze the file names to determine the MIME type by extracting the extension from the file name. If the extension matches one in our table (case insensitive), we return the MIME type; otherwise, we return `UNKNOWN`.

### Explanation:

- We use a dictionary `mime_table` to store the file extensions and their corresponding MIME types, converting extensions to lowercase to handle case insensitivity.
- For each file name, the program finds the last occurrence of a `.` in the string, and extracts the file extension if valid.
- The MIME type is printed if the extension is found in the dictionary, otherwise `UNKNOWN` is printed.

### Edge Cases Handled:

- Files with no extension or a dot at the end.
- Extensions in different cases (e.g., `.TXT`, `.txt`, `.tXt` all map to the same MIME type).
- Files whose extensions aren't in the provided table result in `UNKNOWN`.

## Example Input/Output

**Input**

```
3
3
html text/html
png image/png
gif image/gif
animated.gif
portrait.png
index.html
```

**Output**

```
image/gif
image/png
text/html
```

## Code Example

```python
# Number of elements which make up the association table.
N = int(input())

# Number of file names to be analyzed.
Q = int(input())

mime_table = {}

# Reading the MIME type associations.
for _ in range(N):
    ext, mime_type = input().split()
    mime_table[ext.lower()] = mime_type  # Store extensions as lowercase for case-insensitivity.

# Processing each file name.
for _ in range(Q):
    fname = input()
    
    # Find the position of the last '.' in the file name.
    last_dot_index = fname.rfind('.')
    
    # If there's a '.' and it isn't the last character, extract the extension.
    if last_dot_index != -1 and last_dot_index < len(fname) - 1:
        file_ext = fname[last_dot_index + 1:].lower()  # Get the file extension and convert to lowercase.
        
        # Check if the extension exists in the mime_table.
        if file_ext in mime_table:
            print(mime_table[file_ext])  # Output the MIME type.
        else:
            print('UNKNOWN')  # Output UNKNOWN if extension not found.
    else:
        print('UNKNOWN')  # Output UNKNOWN if no extension or '.' at the end.

```
