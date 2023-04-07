import calculadora_sabermetria as calc

def consola_fip()->None:
    print("*******************************************")
    print("- - - - - Calculador de FIP de un bateador - - - - -")
    print("*******************************************")
    hr = int(input("Ingrese el numero de jonrones del lanzador (HR): "))
    bb = int(input("Ingrese el numero de bases por bolas de un lanzador (BB): "))
    gp = int(input("Ingrese el numero de juegos jugados por el jugador (GP): "))
    ibb = int(input("Ingrese el numero de bases por bolas intencionales del lanzador (IBB): "))
    k = int(input("Ingrese el numero de strike outs logrados por el lanzador (K): "))
    ip = int(input("Ingrese el numero de entradas lanzadas de un de lanzador (IP): "))

    print(f"\nEl FIP del bateador es {calc.redondear_a_tres_decimales(calc.calcular_fip(hr, bb, gp, ibb, k, ip))}")
    print("*******************************************")

consola_fip()