s = input()
leet_s = ""
leet_dict = {'o': '0', 'l': '1', 'z': '2', 'e': '3', 'a': '4', 's': '5', 'g': '6', 't': '7', 'b': '8', 'q': '9'}

for c in s:
    c_lower = c.lower()
    if c_lower in leet_dict:
        leet_s += leet_dict[c_lower]
    else:
        leet_s += c

print(leet_s)
