s = input().lower().split()
count = 0
for word in s:
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
            break
print(count)
