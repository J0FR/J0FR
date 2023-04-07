# https://codeforces.com/problemset/problem/617/A

# Metodo 1
casa_amigo = int(input())
elefante = 0
pasos = 0

while elefante != casa_amigo:
    for _ in range(5, 0, -1):
        if (elefante + _) <= (casa_amigo):
            pasos += 1
            elefante += _
            break

print(pasos)



# Metodo 2
casa_amigo = int(input())
pasos = 0

pasos += casa_amigo // 5
casa_amigo = casa_amigo % 5
pasos += casa_amigo // 4
casa_amigo = casa_amigo % 4
pasos += casa_amigo // 3
casa_amigo = casa_amigo % 3
pasos += casa_amigo // 2
casa_amigo = casa_amigo % 2
pasos += casa_amigo

print(pasos)
