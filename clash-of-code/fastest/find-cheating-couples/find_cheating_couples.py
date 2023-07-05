def find_cheating_couples(n, relationships):
    cheaters_count = 0
    partners = {}

    # Populate the partners dictionary with partners for each person
    for a, b in relationships:
        if a not in partners:
            partners[a] = set()
        if b not in partners:
            partners[b] = set()
        
        partners[a].add(b)
        partners[b].add(a)

    # Count the couples where both partners are cheaters
    for a, b in relationships:
        if len(partners[a]) > 1 and len(partners[b]) > 1:
            cheaters_count += 1
    
    return cheaters_count


if __name__ == '__main__':
    # Read input
    n = int(input())
    relationships = []
    for _ in range(n):
        a, b = map(int, input().split())
        relationships.append((a, b))

    # Calculate and print the result
    result = find_cheating_couples(n, relationships)
    print(result)
