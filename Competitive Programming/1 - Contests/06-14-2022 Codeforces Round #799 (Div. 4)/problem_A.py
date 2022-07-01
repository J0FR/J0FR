# Paso

import sys

test_cases = int(sys.stdin.readline())

for i in range(test_cases):
    lst = list(map(int, sys.stdin.readline().split()))
    contador = 0
    for _ in range(1, 4):
        if lst[0] < lst[_]:
            contador += 1
    print(contador)
    