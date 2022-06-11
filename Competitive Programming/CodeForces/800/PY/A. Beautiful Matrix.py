# https://codeforces.com/problemset/problem/263/A

case = list(map(int, input().split()))
matrix = []
x = 0
y = 0

for _ in range(5):
    matrix.append(case)
    if 1 not in case:
        y += 1
    else:
        y += 1
        x = case.index(1)+1
        break
    case = list(map(int, input().split()))

print(abs(3 - x) + abs(3 - y))