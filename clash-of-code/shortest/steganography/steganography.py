def insert_info(info, image):
    info_idx = 0
    for i in range(len(image)):
        for j in range(len(image[i])):
            if info_idx >= len(info):
                return image  # Return the modified image if all info has been inserted
            pixel = list(bin(image[i][j])[2:].zfill(8))  # Convert pixel to binary string
            pixel[-1] = info[info_idx]  # Replace least significant bit with info bit
            image[i][j] = int("".join(pixel), 2)  # Convert binary string back to integer pixel value
            info_idx += 1
    return image


if __name__ == "__main__":
    # Read inputs
    info = input().strip()
    w, h = map(int, input().strip().split())
    image = []
    for _ in range(h):
        pixels = list(map(int, input().strip().split()))
        image.append(pixels)

    # Insert information into the image
    modified_image = insert_info(info, image)

    # Print the modified image
    for row in modified_image:
        print(" ".join(map(str, row)))
