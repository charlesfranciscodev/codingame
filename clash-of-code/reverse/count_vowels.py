sentence = input().split()

vowels = ['a', 'e', 'i', 'o', 'u']

counts = []
for word in sentence:
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    counts.append(str(count))

print(' '.join(counts))
