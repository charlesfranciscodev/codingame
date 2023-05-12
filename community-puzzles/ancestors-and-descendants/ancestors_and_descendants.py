def print_tree(tree):
    output = ""
    if not tree:
        return
    i = 0
    while i < len(tree) - 1:
        output += tree[i] + " > "
        i += 1
    output += tree[i]
    print(output)


nb_people = int(input())
tree = []  # partial family tree

for _ in range(nb_people):
    line = input().strip()
    name = line.replace(".", "").rstrip()
    name_level = len(line) - len(name)
    tree_level = len(tree)
    
    if name_level == 0:
        if tree:
            print_tree(tree)
            tree.clear()
    elif name_level < tree_level:
        print_tree(tree)
        while name_level < len(tree):
            tree.pop()
    
    tree.append(name)

print_tree(tree)
