# Rumor
import sys

n, m = list(map(int, sys.stdin.readline().split()))
gold_cost = list(map(int, sys.stdin.readline().split()))
gold_costDict = {}
for _ in range(1, n + 1):
    gold_costDict[_] = gold_cost[_ - 1]

conjuntos = []

if m == 0:
        print(sum(gold_cost))

for _ in range(m):
    if  m != 0:
        a, b = map(int, sys.stdin.readline().split())
        if len(conjuntos) != 0:
            agregado = 0
            for conjunto in conjuntos:
                if a in conjunto and b not in conjunto:
                    conjunto.append(b)
                    agregado += 1 
                if b in conjunto and a not in conjunto:
                    conjunto.append(a)
                    agregado += 1 
            if agregado == 0:
                conjuntos.append([a, b])
        else:
            conjuntos.append([a, b])


suma = 0
faltantes = []
if  m != 0:
    for _ in conjuntos:
        lst = []
        for i in _:
            lst.append(gold_costDict[i])
        suma += min(lst)

    for i in range(1, n + 1):
        count = 0
        for _ in conjuntos:
            if i in _:
                count += 1
                break
        if count == 0:
            faltantes.append(i)

    for _ in faltantes:
        value = gold_costDict[_]
        suma += value
    print(suma)



