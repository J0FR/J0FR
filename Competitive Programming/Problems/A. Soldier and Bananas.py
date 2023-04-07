# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())
money_needed = 0 

for _ in range(1, w+1):
    money_needed += _*k

answer = None

if money_needed > n:
    answer = money_needed - n
else:
    answer = 0

print(answer)
