# https://codeforces.com/problemset/problem/160/A

number_of_coins = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
brother1 = []

for _ in range(len(coins)):
    while sum(brother1) <= sum(coins):
        brother1.append(coins.pop(0))

print(len(brother1))
