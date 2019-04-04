if __name__ == "__main__":
    width = int(input())
    height = int(input())
    text = input().upper()
    for _ in range(height):
        row = input()
        output = ""
        for character in text:
            position = ord(character) - ord('A')
            if position < 0 or position > 25:
                position = 26
            start = position * width
            end = start + width
            output += row[start:end]
        print(output)
