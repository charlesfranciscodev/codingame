# Mime Type

This is a solution to the "Mime Type" problem on [Codingame](https://www.codingame.com/training/easy/mime-type).

## Problem Description

You are given a list of file names and their corresponding MIME types. You need to read a list of file names and determine the corresponding MIME type for each file name. If the MIME type cannot be determined, the program should output `UNKNOWN`.

The MIME type is determined by the file extension. The table of file extensions and their corresponding MIME types is given.

| Extension | MIME Type |
|-----------|-----------|
|html       |text/html  |
|htm        |text/html  |
|png        |image/png  |
|jpeg       |image/jpeg |
|jpg        |image/jpeg |
|gif        |image/gif  |
|bmp        |image/bmp  |
|txt        |text/plain|
|pdf        |application/pdf|

The file name may have multiple periods (.) in it, but the extension is always the substring that follows the last period.

## Solution

The solution reads the the number of MIME types, number of file names and the file names. It stores the MIME types in a map with the extension as the key. Then it reads a list of file names and determines the corresponding MIME type by looking up the extension in the map. If the extension is not found, it outputs `UNKNOWN`.

## Example Input/Output

Input:

```
4
2
html text/html
png image/png
gif image/gif
txt text/plain
file.html
file.txt
```

Output:

```
text/html
text/plain
```

## Example Code

```python
# Read the number of elements in the association table
n = int(input())

# Read the number of file names to be analyzed
q = int(input())

# Create a dictionary to store the association table
mime_types = {}

# Read the association table
for _ in range(n):
    ext, mime = input().split()
    mime_types[ext.lower()] = mime

# Process each file name
for _ in range(q):
    file_name = input().lower()

    # Find the extension of the file
    if '.' in file_name:
        extension = file_name.split('.')[-1]
        if extension in mime_types:
            print(mime_types[extension])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")

```
