# https://codeforces.com/problemset/problem/231/A

cases = int(input())
works = 0

while cases != 0:
    case = list(map(int, input().split()))
    if sum(case) >= 2:
        works += 1
    cases -= 1

print(works)