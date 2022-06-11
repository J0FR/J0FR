# https://codeforces.com/problemset/problem/71/A

cases = int(input())

while cases != 0:
    case = input()
    if len(case) > 10:
        print(f"{case[0]}{len(case)-2}{case[-1]}")
    else:
        print(case)
    cases-= 1