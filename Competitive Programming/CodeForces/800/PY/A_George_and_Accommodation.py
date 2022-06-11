import sys

cases = int(sys.stdin.readline())
counter = 0

for _ in range(cases):
    p, q = map(int, sys.stdin.readline().split())
    if p + 2 <= q:
        counter += 1

print(counter)
