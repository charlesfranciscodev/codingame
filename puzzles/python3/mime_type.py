from typing import Dict


if __name__ == "__main__":
    table: Dict[str, str] = {}  # file extension => mime type
    nb_elements: int = int(input())
    nb_names: int = int(input())

    for _ in range(nb_elements):
        extension, mime_type = input().split()
        table[extension.lower()] = mime_type

    for _ in range(nb_names):
        name: str = input().lower()
        dot_index: int = name.rfind(".")
        if dot_index == -1 or dot_index == len(name) - 1:
            print("UNKNOWN")
        else:
            extension: str = name[dot_index + 1:]
            if extension in table:
                print(table[extension])
            else:
                print("UNKNOWN")
