def generate_leetspeak_variants(word):
    leet_dict = {'A': '4', 'E': '3', 'I': '1', 'L': '1', 'T': '7', 'O': '0'}
    variants = set()

    def generate_variants(current_variant, remaining_chars):
        if not remaining_chars:
            variants.add(current_variant)
            return

        char, rest = remaining_chars[0], remaining_chars[1:]
        if char.upper() in leet_dict:
            generate_variants(current_variant + leet_dict[char.upper()], rest)

        generate_variants(current_variant + char, rest)

    generate_variants('', word)
    return sorted(variants)


if __name__ == "__main__":
    # Input
    word = input().strip()

    # Output
    variants = generate_leetspeak_variants(word)
    for variant in variants:
        print(variant)
