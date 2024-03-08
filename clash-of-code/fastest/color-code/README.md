## Color Name Identifier

This Python script (`name_color.py`) is designed to identify the name of a color based on its RGB code.

### Problem Description

Given a hexadecimal color code, the program determines the name of the corresponding color. It categorizes colors into specific names such as black, white, red, green, blue, magenta, yellow, cyan, or grey based on the intensity of their RGB values.

### Solution Summary

The `name_color` function takes a hexadecimal color code as input and extracts its RGB values. It then applies a set of conditions to determine the name of the color based on its intensity. Here's a summary of the color categorization logic:

- **Black**: All RGB values are less than 10.
- **White**: All RGB values are greater than or equal to 245.
- **Primary Colors**: If one RGB value is greater than or equal to 10 and the other two are less than 10, the color is identified as red, green, or blue depending on which value is greater.
- **Secondary Colors**: If two RGB values are greater than or equal to 10 and the other one is less than 10, the color is identified as magenta, yellow, or cyan based on the combination of the high-value components.
- **Grey**: All other cases not covered by the above conditions are considered as grey.

The script includes an example usage where the user is prompted to input a hexadecimal color code, and the corresponding color name is printed.

### Usage

1. Run the script `name_color.py`.
2. Input a hexadecimal color code when prompted.
3. The script will output the corresponding color name.
