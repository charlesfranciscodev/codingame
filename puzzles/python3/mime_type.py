from typing import Dict


if __name__ == "__main__":
    table: Dict[str, str] = {}  # file extension => mime type
    nb_elements = int(input())
    nb_names = int(input())

    for _ in range(nb_elements):
        extension, mime_type = input().split()
        table[extension.lower()] = mime_type

    for _ in range(nb_names):
        name = input().lower()
        dot_index = name.rfind(".")
        if dot_index == -1 or dot_index == len(name) - 1:
            print("UNKNOWN")
        else:
            extension = name[dot_index + 1:]
            if extension in table:
                print(table[extension])
            else:
                print("UNKNOWN")
