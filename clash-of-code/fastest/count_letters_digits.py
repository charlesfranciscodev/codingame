s = input()
count_letters = 0
count_digits = 0
for c in s:
    if c.isalpha():
        count_letters +=1
    elif c.isdigit():
        count_digits += 1
print(round(count_letters / count_digits))
