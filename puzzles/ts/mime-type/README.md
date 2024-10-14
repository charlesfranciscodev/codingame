# MIME Type

## Description

The task involves creating a program to determine the MIME type of files based on their names. This involves associating file extensions with MIME types. The program reads an association table with N elements and a list of Q file names to be analyzed. For each file name, the program identifies the extension by finding the substring after the last dot character. If the extension is found in the association table (case insensitive), it prints the corresponding MIME type. If the MIME type cannot be determined or the file has no extension, it outputs UNKNOWN. The program takes the number of elements in the table, the number of file names, the extension-MIME associations, and the file names as input, and outputs the corresponding MIME types or UNKNOWN.

## Solution Overview

To solve this problem, we need to map file extensions to their respective MIME types, and then analyze the file names to determine the MIME type by extracting the extension from the file name. If the extension matches one in our table (case insensitive), we return the MIME type; otherwise, we return `UNKNOWN`.

### Explanation:

1. **Input Parsing:**
   - The number of MIME type associations (`N`) and the number of file names to analyze (`Q`) are read first.
   - Then, the MIME type associations are stored in an object (`mimeTable`), where the key is the file extension and the value is the MIME type. Extensions are stored in lowercase to ensure case insensitivity.

2. **File Name Analysis:**
   - For each file name, we determine if it has a valid extension by checking for the last occurrence of a `.` (dot) character.
   - If the file has an extension (i.e., the `.` is not the last character), we extract the extension, convert it to lowercase, and look it up in the MIME type table.
   - If the extension exists in the table, the corresponding MIME type is printed; otherwise, `UNKNOWN` is printed.

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

```typescript
const N: number = parseInt(readline()); // Number of elements which make up the association table.
const Q: number = parseInt(readline()); // Number Q of file names to be analyzed.

const mimeTable: { [key: string]: string } = {};

// Reading the MIME type associations.
for (let i = 0; i < N; i++) {
    const inputs: string[] = readline().split(' ');
    const EXT: string = inputs[0].toLowerCase(); // file extension (converted to lowercase for case-insensitivity)
    const MT: string = inputs[1]; // MIME type
    mimeTable[EXT] = MT; // Store the MIME type with the extension as the key
}

// Processing each file name.
for (let i = 0; i < Q; i++) {
    const FNAME: string = readline();
    
    // Find the position of the last '.' in the file name.
    const lastDotIndex = FNAME.lastIndexOf('.');

    // If there's a '.' and it isn't the last character, extract the extension.
    if (lastDotIndex !== -1 && lastDotIndex < FNAME.length - 1) {
        const fileExt = FNAME.slice(lastDotIndex + 1).toLowerCase(); // Get the file extension and convert to lowercase
        
        // Check if the extension exists in the mimeTable.
        if (mimeTable.hasOwnProperty(fileExt)) {
            console.log(mimeTable[fileExt]); // Output the MIME type
        } else {
            console.log('UNKNOWN'); // Output UNKNOWN if extension not found
        }
    } else {
        console.log('UNKNOWN'); // Output UNKNOWN if no extension or '.' at the end
    }
}

```
