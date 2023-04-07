cases = int(input())
cubes = list(map(int, input().split()))

for _ in range(cases-1, -1, -1):
    for i in range(cases-1, -1, -1):
        if cubes[_] > cubes[i]:
            resta = cubes[_] - cubes[i]
            cubes[i] += resta
            cubes[_] -= resta

print(" ".join(map(str, cubes)))