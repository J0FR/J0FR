import calculadora_sabermetria as calc

def consola_ops()->None:
    print("*******************************************")
    print("- - - - - Calcular OPS jugador - - - - -")
    print("*******************************************")
    sencillos = int(input("Ingrese el numero de bases sencillas alcanzadas por el bateador (Sencillos): "))
    dobles = int(input("Ingrese el numero de bases dobles alcanzadas por el bateador (Dobles): "))
    triples = int(input("Ingrese el numero de bases triples alcanzados por el bateador (Triples): "))
    hr = int(input("Ingrese el numero de bases triples alcanzados por el bateador (HR): "))
    h = int(input("Ingrese el numero de hits conectados del bateador (H): "))
    bb = int(input("Ingrese el numero de bases por bolas del bateador (BB): "))
    gp = int(input("Ingrese el numero de juegos jugados por el jugador (GP): "))
    vb = int(input("Ingrese el numero de turnos de bateo del bateador (VB): "))
    sh = int(input("Ingrese el numero de toques de sacrificio ejectuados por el bateador (SH): "))
    
    print(f"\nEl OPS del jugador es {calc.redondear_a_tres_decimales(calc.calcular_ops(sencillos, dobles, triples, hr, h, bb, gp, vb, sh))}")
    print("*******************************************")

consola_ops()