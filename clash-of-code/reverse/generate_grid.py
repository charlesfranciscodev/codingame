height = int(input())
width = int(input())


def generate_grid(rows, columns):
    output = ""
    for i in range(rows):
        row = ''
        for _ in range(columns):
            row += 'O'
        output += row
        if i < rows - 1:
            output += '\n'
    return output

print(generate_grid(height, width))
