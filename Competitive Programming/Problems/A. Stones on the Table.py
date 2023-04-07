# https://codeforces.com/problemset/problem/266/A

n = int(input())
case = list(input())
case_copy = case.copy()
flag = None
contador = 0

for _ in range(0, n):
    if flag == None or flag != case[_]:
        flag = case[_]
    elif case[_] == flag:
        contador += 1

print(contador)