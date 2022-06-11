# https://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split())
order = list(input())

for _ in range(t):
    i = 1
    while i < n:
        if order[i] == "G" and order[i - 1] == "B":
            order[i], order[i - 1] = order[i - 1], order[i]
            i += 1
        i += 1

print("".join(order))
