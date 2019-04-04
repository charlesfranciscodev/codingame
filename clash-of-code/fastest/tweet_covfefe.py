tweet = input().split()
selected = ""
index = -1
for i, word in enumerate(tweet):
    if word[0] == 'c':
        if len(word) >= len(selected):
            selected = word
            index = i
if index != -1:
    tweet[index] = "covfefe"
print(' '.join(tweet), end='')
if index == -1:
    print("covfefe", end='')
