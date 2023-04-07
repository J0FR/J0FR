import calculadora_sabermetria as calc

def consola_slg()->None:
    print("*******************************************")
    print("- - - - - Calcular SLG jugador - - - - -")
    print("*******************************************")
    sencillos = int(input("Ingrese el numero de bases sencillas alcanzadas por el bateador (sencillos): "))
    dobles = int(input("Ingrese el numero de bases dobles alcanzadas por el bateador (dobles): "))
    triples = int(input("Ingrese el numero de bases triples alcanzados por el bateador (triples): "))
    hr = int(input("Ingrese el numero de bases triples alcanzados por el bateador (HR): "))
    vb = int(input("Ingrese el numero de veces al bate del bateador (VB): "))
    
    print(f"\nEl SLG del jugador es {calc.redondear_a_tres_decimales(calc.calcular_slg(sencillos, dobles, triples, hr, vb))}")
    print("*******************************************")

consola_slg()