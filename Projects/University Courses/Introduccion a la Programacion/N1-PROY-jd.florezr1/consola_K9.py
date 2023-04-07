import calculadora_sabermetria as calc

def consola_k9()->None:
    print("*******************************************")
    print("- - - - - Calculadora de valor K9 para lanzador - - - - -")
    print("*******************************************")
    k = int(input("Ingrese el numero de out por strike del lanzador (K): "))
    ip = int(input("Ingrese el numero de entradas lanzadas por el lanzador (IP): "))

    print(f"\nEl valor K9 del lanzador para el lanzador es {calc.redondear_a_tres_decimales(calc.calcular_k9(k, ip))}")
    print("*******************************************")

consola_k9()