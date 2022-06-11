# https://codeforces.com/problemset/problem/110/A

case = input()

if 4 == (case.count("7") + case.count("4")) or 7 == (case.count("7") + case.count("4")):
    print("YES")
else:
    print("NO")