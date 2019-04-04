char_count = int(input())
count = 0
for i in input().split():
    char_code = int(i)
    print(chr(char_code), end='')
    count += 1
