import calculadora_sabermetria as calc

def consola_obp()->None:
    print("*******************************************")
    print("- - - - - Calcular OBP jugador - - - - -")
    print("*******************************************")
    h = int(input("Ingrese el numero de hits conectados del bateador (H): "))
    bb = int(input("Ingrese el numero de bases por bolas del bateador (BB): "))
    gp = int(input("Ingrese el numero de juegos jugados del jugador (GP): "))
    vb = int(input("Ingrese el numero de turnos de bateo del bateador (VB): "))
    sh = int(input("Ingrese el numero de toques de sacrificio ejecutados por el bateador (SH): "))
    
    print(f"\nEl OBP del jugador es {calc.redondear_a_tres_decimales(calc.calcular_obp(h, bb, gp, vb, sh))}")
    print("*******************************************")

consola_obp()