# no paso

import sys

test_cases = int(sys.stdin.readline())

for i in range(test_cases):
    matriz = []
    for _ in range(9):
        val = sys.stdin.readline()
        if val != "\n":
            lst = list(val.strip())
            matriz.append(lst)
    contador = 0
    found = False
    x = 0
    y = 0
    for x in range(8):
        if found:
            break
        for y in range(8):
            
            if matriz[x][y] != "#":
                continue
            else:
                verificar1 = False if x+1 > 7 or y+1 > 7 else True
                verificar2 = False if x-1 > 7 or y+1 > 7 else True
                verificar3 = False if x+1 > 7 or y-1 > 7 else True
                verificar4 = False if x-1 > 7 or y-1 > 7 else True
                    
                if verificar1 and matriz[x+1][y+1] == "#":
                    contador += 1
                else:
                    contador = 0
                    continue
                if verificar2 and matriz[x-1][y+1] == "#":
                    contador += 1
                else:
                    contador = 0
                    continue
                if verificar3 and matriz[x+1][y-1] == "#":
                    contador += 1
                else:
                    contador = 0
                    continue
                if verificar4 and matriz[x-1][y-1] == "#":
                    contador += 1
                else:
                    contador = 0
                    continue
                if contador == 4:

                    print(f'{(x + 1)} {(y + 1)}')
                    found = True
                    break
    