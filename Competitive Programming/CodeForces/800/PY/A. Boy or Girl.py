# https://codeforces.com/problemset/problem/236/A

name = input()
different_characters = []

for _ in name:
    if _ not in different_characters:
        different_characters.append(_)

if (len(different_characters) % 2) == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")