if __name__ == "__main__":
    n = int(input())
    trie: dict = {}
    nb_elements = 0  # number of elements (referencing a number) stored in the structure
    for _ in range(n):
        phone_number = input()
        current_node: dict = trie
        for digit in phone_number:
            if digit in current_node:
                current_node = current_node[digit]
            else:
                current_node[digit] = {}
                current_node = current_node[digit]
                nb_elements += 1
    print(nb_elements)
