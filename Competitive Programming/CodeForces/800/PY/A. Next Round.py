# https://codeforces.com/problemset/problem/158/A

start = list(map(int, input().split()))
case = list(map(int, input().split()))
k = case[start[1] - 1]
work = 0

for i in range(3):
    work = 0
    for _ in case:
        if _ > 0 and _ >= k:
            work += 1

print(work)