import calculadora_sabermetria as calc

def consola_babip()->None:
    print("*******************************************")
    print("- - - - - Calculadora de valor BABIP del bateador - - - - -")
    print("*******************************************")
    hr = int(input("Ingrese el numero de jonrones del lanzador (HR): "))
    h = int(input("Ingrese el numero de hits conectados por el bateador cuando el lanzador pone la pelota (H): "))
    k = int(input("Ingrese el numero de out por strike del lanzador (K): "))
    sf = int(input("Ingrese el numero de bases por bolas intencionales del lanzador (SF): "))
    tb = int(input("Ingrese el numero de turnos de bateo (TB): "))

    print(f"\nEl valor BABIP del bateador es {calc.redondear_a_tres_decimales(calc.calcular_babip(hr, h, k, sf, tb))}")
    print("*******************************************")

consola_babip()