def calcular_obp(h: int, bb: int, gp: int, vb: int, sh: int)-> float :
    """
    Descripcion Funcion:
        Realiza el cálculo del OBP de un bateador.

    Parametros:
        H (int) | El número de hits conectados del bateador.
        BB (int) | El número de bases por bolas del bateador.
        GP (int) | El número de juegos jugados del jugador.
        VB (int) | El número de turnos de bateo del bateador.
        SH (int) | El número de toques de sacrificio ejecutados por el bateador.

    Retorna:
        float: Un float que represente la estadística del OBP del bateador, calculado a
               partir de los valores ingresados por parámetro.
    """

    return ((h + bb + gp) / (vb + bb + gp - sh))


def bases_en_miles(sencillos: int, dobles: int, triples: int, hr: int) -> int:
    """
    Descripcion Funcion:
        Calcula el valor de las bases alcanzadas por un bateador en miles. Recuerde
        que una base sencilla equivale a 1000 puntos, una doble equivale a 2000,
        una triple a 3000 y un jonrón a 4000.

    Parametros:
        sencillos (int) | El número de bases sencillas alcanzadas por el bateador. (En unidades)
        dobles (int) | El número de bases dobles alcanzadas por el bateador. (En unidades)
        triples (int) | El número de bases triples alcanzados por el bateador. (En unidades)
        HR (int) | El número de jonrones realizados por el bateador. (En unidades)

    Retorna:
        int: Puntaje total según todas las bases y jonrones realizados por un bateador, en miles.
    """
    
    return (((sencillos) + (dobles * 2) + (triples * 3) + (hr * 4)) * 1000)


def calcular_slg(sencillos: int, dobles: int, triples: int, hr: int, vb: int) -> float:
    """
    Descripcion Funcion:
        Calcula el valor de la estadística de Slugging para un bateador que tiene los
        valores ingresados por parámetro.

    Parametros:
        sencillos (int) | El número de bases sencillas alcanzadas por el bateador. (En unidades)
        dobles (int) | El número de bases dobles alcanzadas por el bateador. (En unidades)
        triples (int) | El número de bases triples alcanzados por el bateador. (En unidades)
        HR (int) | El número de jonrones realizados por el bateador. (En unidades)
        VB (int) | El número de veces al bate del bateador.

    Retorna:
        float: Un float que represente la estadística de Slugging para un bateador con los
               valores ingresados por parámetro.
    """

    return (bases_en_miles(sencillos, dobles, triples, hr) / (vb * 1000))


def calcular_ops(sencillos: int, dobles: int, triples: int, hr: int, h: int, bb: int, gp: int, vb: int, sh: int) -> float:
    """
    Descripcion Funcion:
        Calcula el valor de la estadística de OPS para un bateador con los valores
        ingresados por parámetro.

    Parametros:
        sencillos (int) | El número de bases sencillas alcanzadas por el bateador. (En unidades)
        dobles (int) | El número de bases dobles alcanzadas por el bateador. (En unidades)
        triples (int) | El número de bases triples alcanzados por el bateador. (En unidades)
        HR (int) | El número de jonrones realizados por el bateador. (En unidades)
        H (int) | El número de hits conectados del bateador.
        BB (int) | El número de bases por bolas del bateador.
        GP (int) | El número de juegos jugados del jugador
        VB (int) | El número de turnos de bateo del bateador
        SH (int) | El número de toques de sacrificio ejecutados por el bateador.

    Retorna:
        float: Un float que represente el valor de la estadística de OPS para un bateador
               con los valores ingresados por parámetro.
    """

    return (calcular_obp(h, bb, gp, vb, sh) + calcular_slg(sencillos, dobles, triples, hr, vb))


def calcular_k9(k: int, ip:int) -> float:
    """
    Descripcion Funcion:
        Calcula el valor de la estadística de K/9 para un lanzador con los valores
        ingresados por parámetro.

    Parametros:
        K (int) | El número de out por strike del lanzador
        IP (int) | El número de entradas lanzadas por el lanzador.

    Retorna:
        float: El valor de la estadística K/9 para un lanzador, calculado a partir de los
               valores ingresados por parámetro.
    """

    return ((k/ip) * 9) 


def calcular_fip(hr: int, bb: int, gp: int, ibb: int, k: int, ip: int) -> float:
    """
    Descripcion Funcion:
        Realiza el cálculo del FIP de un bateador

    Parametros:
        HR (int) | El número de jonrones del lanzador.
        BB (int) | El número de bases por bolas de un lanzador
        GP (int) | El número de juegos jugados por el jugador.
        IBB (int) | El número de bases por bolas intencionales del lanzador
        K (int) | El número de strike outs logrados por el lanzador.
        IP (int) | El número de entradas lanzadas de un lanzador

    Retorna:
        float: Un float que represente la estadística del FIP del bateador, calculado a partir
               de los valores ingresados por parámetro.
    """

    return ((hr * 13 + (bb + gp - ibb) * 3 - k * 2) / (ip))


def calcular_babip(hr: int, h: int, k: int, sf: int, tb: int) -> float:
    """
    Descripcion Funcion:
        Realiza el cálculo del BABIP de un bateador.

    Parametros:
        HR (int) | El número de jonrones del lanzador
        H (int) |El número de hits conectados por el bateador cuando el lanzador pone la pelota.
        K (int) | El número de out por strike del lanzador.
        SF (int) | El número de bases por bolas intencionales del lanzador.
        TB (int) | El número de turnos de bateo. El número de turnos de bateo es diferente a
                   las veces al bate (VB). Refiérase a la descripción del BABIP para mirar como
                   calcular el VB a partir de los turnos de bateo, los out por strike y los jonrones.

    Retorna:
        float: Un float que represente la estadística del BABIP del bateador, calculado a
               partir de los valores ingresados por parámetro.
    """

    return ((h - hr) / ((tb - k - hr) - hr - k + sf))


def redondear_a_tres_decimales(numero: float)->str:
    """
    Descripcion Funcion:
        Redondea a cualquier float a 3 decimales.

    Parametros:
        numero (float) | Numero que se desea redondear.

    Retorna:
        str: Un str que dice el numero insertado redondeado a 3 decimales.
    """

    return format(round((numero), 3), ".3f")