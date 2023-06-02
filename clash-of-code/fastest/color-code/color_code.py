def name_color(code):
    # Extract RGB values from the color code
    red = int(code[1:3], 16)
    green = int(code[3:5], 16)
    blue = int(code[5:7], 16)

    # Check if all values are < 10 (black)
    if red < 10 and green < 10 and blue < 10:
        return "black"

    # Check if all values are >= 245 (white)
    if red >= 245 and green >= 245 and blue >= 245:
        return "white"

    # Check if one value is >= 10 and the other two are < 10 (high-value color)
    if (red >= 10 and green < 10 and blue < 10) or \
       (red < 10 and green >= 10 and blue < 10) or \
       (red < 10 and green < 10 and blue >= 10):
        if red >= 10:
            return "red"
        elif green >= 10:
            return "green"
        else:
            return "blue"

    # Check if two colors are >= 10 and the other is < 10 (secondary colors)
    if (red >= 10 and green >= 10 and blue < 10) or \
       (red >= 10 and green < 10 and blue >= 10) or \
       (red < 10 and green >= 10 and blue >= 10):
        if red >= 10 and blue >= 10:
            return "magenta"
        elif red >= 10 and green >= 10:
            return "yellow"
        else:
            return "cyan"

    # All other cases are considered as grey
    return "grey"


if __name__ == "__main__":
    # Example usage
    color_code = input()
    color_name = name_color(color_code)
    print(color_name)
