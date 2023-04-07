"""
Ejercicio nivel 2: Cálculo de velocidades en vías colombianas
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

"""


def crear_sector( nombre: str, carriles: int, pendiente: float, 
                   ancho_calzada: float, ancho_berma: float, separador: bool,
                   peatones: bool, control_accesos: str, 
                   zona_recreacional: bool,cuello_de_botella: bool, 
                   zona_escolar: bool ) -> dict:
    """
    Crea un diccionario que representa un sector de la vía con todos sus 
    atributos inicializados.
    
    Parámetros
    ----------
    nombre : str
        Nombre del sector vial.
    carriles : int
        Número de carriles dentro del sector.
    pendiente : float
        Porcentaje de inclinación del sector.
    ancho_calzada : float
        Ancho en metros de la calzada del sector.
    ancho_berma : float
        Ancho en metros de la berma del sector.
    separador : bool
        Existencia de un separador en el sector.
    peatones : bool
        Existencia de concentración de peatones en el sector.
    control_accesos : str
        Tipo de control de accesos que hay en una vía.
        Puede ser “Total”, “Parcial” o “Nulo”
    zona_recreacional : bool
        Existencia de una zona recreacional en el sector.
    cuello_de_botella : bool
        Existencia de un cuello de botella en el sector.
    zona_escolar : bool
        Existencia de una zona escolar en el sector.

    Retorno
    -------
    dict
        Diccionario del sector vial con sus características.

    """
    sector_de_la_via = {
        "nombre": nombre, 
        "carriles": carriles, 
        "pendiente": pendiente, 
        "ancho_calzada": ancho_calzada, 
        "ancho_berma": ancho_berma, 
        "separador": separador, 
        "peatones": peatones, 
        "control_accesos": control_accesos, 
        "zona_recreacional": zona_recreacional, 
        "cuello_de_botella": cuello_de_botella, 
        "zona_escolar": zona_escolar
        }

    return sector_de_la_via


def buscar_sector( nombre: str, s1: dict, s2: dict, s3: dict, 
                  s4: dict ) -> dict:
    """
    Busca el sector vial que coincide con el nombre pasado por parámetro.
    Si no se encuentra el sector, se retorna None.
    
    Parámetros
    ----------
    nombre : str
        Nombre del sector vial.
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    dict
        Diccionario del sector vial con el nombre dado por parámetro.
        Retorna None si no lo encuentra.

    """
    sector = ""
    if s1["nombre"].lower() == nombre.lower():
        sector = s1
    elif s2["nombre"].lower() == nombre.lower():
        sector = s2
    elif s3["nombre"].lower() == nombre.lower():
        sector = s3
    elif s4["nombre"].lower() == nombre.lower():
        sector = s4
        
    return sector
    

def clasificar_sector( sector: dict ) -> str:
    """
    Clasifica un sector según sus características geométricas.

    Parámetros
    ----------
    sector : dict
        Diccionario del sector vial a clasificar.

    Retorno
    -------
    str
        Retorna alguna de las 7 clasificaciones viales según características
        geométricas (A1,B1,C1,A2,B2,C2 o D2).

    """
    tipo_de_sector = ""
    # VIA MULTICARRIL
    #A1
    if (sector["pendiente"] <= 0.05) and (sector["ancho_calzada"] == 7.30) and (sector["ancho_berma"] == 2.50):
        tipo_de_sector = "A1"
    #B1
    elif (sector["pendiente"] <= 0.06) and (sector["ancho_calzada"] == 7.30) and (sector["ancho_berma"] == 1.50):
        tipo_de_sector = "B1"
    #C1
    elif (sector["pendiente"] <= 0.08) and (sector["ancho_calzada"] == 7.00) and (sector["ancho_berma"] == 1.30):
        tipo_de_sector = "C1"

# Sector de 2 carriles
    elif (sector["separador"] == False) and (sector["control_accesos"] == "Nulo"):
        #A1
        if  (sector["pendiente"] <= 0.06) and (sector["ancho_calzada"] == 7.30) and (sector["ancho_berma"] == 1.80):
            tipo_de_sector = "A2"
        #B2
        elif (sector["pendiente"] <= 0.08) and (sector["ancho_calzada"] == 7.30) and (sector["ancho_berma"] == 1.00):
            tipo_de_sector = "B2"
        #C2
        elif (sector["pendiente"] <= 0.09) and (sector["ancho_calzada"] == 7.00) and (sector["ancho_berma"] == 0.50):
            tipo_de_sector = "C2"
        #D2
        elif (sector["pendiente"] <= 0.09) and (sector["ancho_calzada"] == 7.00) and (sector["ancho_berma"] == 0.40):
            tipo_de_sector = "D2"
    
    return tipo_de_sector


def determinar_velocidad_generica( sector: dict ) -> int:
    """
    Determina la velocidad genérica del sector según sus características.

    Parámetros
    ----------
    sector : dict
        Diccionario del sector vial a analizar.

    Retorno
    -------
    int
        Velocidad genérica del sector vial en km/h.

    """
    velocidad_generica = 0
    tipo_de_sector = clasificar_sector(sector)

    # Multicarril
    if (tipo_de_sector == "A1") and (sector["control_accesos"] == "Total") and (sector["peatones"] == False) and (sector["separador"] == True):
        velocidad_generica = 120
    elif (tipo_de_sector == "B1"):
        if (sector["control_accesos"] == "Parcial") and (sector["peatones"] == False):
            if (sector["separador"] == True):
                velocidad_generica = 100
            else: 
                velocidad_generica = 90
        elif (sector["control_accesos"] == "Nulo") and (sector["peatones"] == False):
            if (sector["separador"] == True):
                velocidad_generica = 90
            else:
                velocidad_generica = 80 

    elif (tipo_de_sector == "C1"):
        if (sector["control_accesos"] == "Nulo") and (sector["peatones"] == False):
            if (sector["separador"] == True):
                velocidad_generica = 80
            else:
                velocidad_generica = 70    
        elif (sector["control_accesos"] == "Nulo") and (sector["peatones"] == True):
            if (sector["separador"] == True):
                velocidad_generica = 70
            else: 
                velocidad_generica = 60
            
    # Dos Carriles
    elif (sector["separador"] == False) and (sector["control_accesos"] == "Nulo"):
        if (tipo_de_sector == "A2"):
            if (sector["peatones"] == False):
                velocidad_generica = 80
            else:
                velocidad_generica = 70
        elif (tipo_de_sector == "B2"):
            if (sector["peatones"] == False):
                velocidad_generica = 70
            else: 
                velocidad_generica = 60
        elif (tipo_de_sector == "C2") and (sector["peatones"] == True):
            velocidad_generica = 50
        elif (tipo_de_sector == "D2") and (sector["peatones"] == True):
            velocidad_generica = 40

    return velocidad_generica


def calcular_velocidad_promedio( sector: dict ) -> float:
    """
    Calcula la velocidad promedio de un sector según sus restricciones por
    sitios especiales.

    Parámetros
    ----------
    sector : dict
        Diccionario del sector vial a analizar.

    Retorno
    -------
    float
        Velocidad promedio del sector en km/h redondeada a 2 cifras decimales.

    """
    # TODO: completar y r emplazar la siguiente linea por el resultado correcto
    sumatoria_valocidad = determinar_velocidad_generica(sector)
    numero_sitios_especiales = 0

    if sector["zona_recreacional"] == True:
        sumatoria_valocidad += 30
        numero_sitios_especiales += 1
    if sector["cuello_de_botella"] == True:
        sumatoria_valocidad += 40
        numero_sitios_especiales += 1
    if sector["zona_escolar"] == True:
        sumatoria_valocidad += 30
        numero_sitios_especiales += 1
    
    velocidad_promedio = (sumatoria_valocidad)/(numero_sitios_especiales + 1)

    return round(velocidad_promedio, 2)


def contar_libres_de_restriccion( s1: dict, s2: dict, s3: dict,
                                 s4: dict ) -> int:
    """
    Cuenta los sectores que no tienen sitios especiales.

    Parámetros
    ----------
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    int
        Número de sectores que no tienen sitios especiales.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    contador = 0
    if no_tiene_sitio_especial(s1) == True:
        contador += 1
    if no_tiene_sitio_especial(s2) == True:
        contador += 1
    if no_tiene_sitio_especial(s3) == True:
        contador += 1
    if no_tiene_sitio_especial(s4) == True:
        contador += 1

    return contador

def no_tiene_sitio_especial(sector: dict) -> bool:
    """
    Dice si tiene sitios especiales o no.

    Parámetros
    ----------
    sector : dict
        Diccionario con la información del sector vial.

    Retorno
    -------
    bool
        True si no tiene sitios especiales - False si tiene sitios especiales.

    """
    if (sector["zona_recreacional"] == False) and (sector["cuello_de_botella"] == False) and (sector["zona_escolar"] == False):
        return True
    else:
        return False


def determinar_pendiente_menor( pendiente: float, s1: dict, s2: dict, s3: dict,
                               s4: dict ) -> str:
    """
    Determina cuáles sectores tienen una pendiente menor a un número dado.

    Parámetros
    ----------
    pendiente : float
        Conta superior de la pendiente de los sectores a encontrar.
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.
        
    Retorno
    -------
    str
        Una cadena con todos los nombres de los sectores que tienen una 
        pendiente inferior a la dada por parámetro.
    
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    sectores_con_pendiente_inferior = ""
    if s1["pendiente"] < pendiente:
        sectores_con_pendiente_inferior += s1["nombre"]
    if s2["pendiente"] < pendiente:
        if len(sectores_con_pendiente_inferior) == 0:
            sectores_con_pendiente_inferior += f"{s2['nombre']}"
        else: 
            sectores_con_pendiente_inferior += f", {s2['nombre']}"
    if s3["pendiente"] < pendiente:
        if len(sectores_con_pendiente_inferior) == 0:
            sectores_con_pendiente_inferior += f"{s3['nombre']}"
        else: 
            sectores_con_pendiente_inferior += f", {s3['nombre']}"
        
    if s4["pendiente"] < pendiente:
        if len(sectores_con_pendiente_inferior) == 0:
            sectores_con_pendiente_inferior += f"{s4['nombre']}"
        else: 
            sectores_con_pendiente_inferior += f", {s4['nombre']}"

    if len(sectores_con_pendiente_inferior) == 0:
            sectores_con_pendiente_inferior += "Ninguno"
            
    return sectores_con_pendiente_inferior


def velocidad_maxima( s1: dict, s2: dict, s3: dict, s4: dict ) -> dict:
    """
    Retorna el diccionario del sector con la velocidad genérica más alta. En
    caso de encontrar dos sectores con la misma velocidad, se debe mostrar el
    nombre del sector que vaya primero alfabéticamente.

    Parámetros
    ----------
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    dict
        El diccionario con la velocidad genérica más alta.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    maxima = s1
    if determinar_velocidad_generica(s2) >= determinar_velocidad_generica(s1):
        if determinar_velocidad_generica(s2) == determinar_velocidad_generica(s1):
            maxima = nombre_primero_alfabeticamente(s1["nombre"], s2["nombre"])
        else:
            maxima = s2
    if determinar_velocidad_generica(s3) >= determinar_velocidad_generica(s2):
        if determinar_velocidad_generica(s3) == determinar_velocidad_generica(s2):
            maxima = nombre_primero_alfabeticamente(s2["nombre"], s3["nombre"])
        else:
            maxima = s3
    if determinar_velocidad_generica(s4) >= determinar_velocidad_generica(s3):
        if determinar_velocidad_generica(s4) == determinar_velocidad_generica(s3):
            maxima = nombre_primero_alfabeticamente(s3["nombre"], s4["nombre"])
        else:
            maxima = s4
    
    return maxima

def nombre_primero_alfabeticamente(s1: str, s2: str) -> dict:
    """
    Retorna el diccionario del sector con el nombre alfabeticamente mas bajo.

    Parámetros
    ----------
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.

    Retorno
    -------
    dict
        El diccionario con que sea alfabeticamente mayor.

    """
    if (s2.lower() > s1.lower()):
        return s1
    else: 
        return s2


def contar_sitios_especiales( s1: dict, s2: dict, s3: dict, s4: dict ) -> dict:
    """
    Retorna un diccionario con la cantidad de sitios especiales que hay en
    todos los sectores.

    Parámetros
    ----------
    s1 : dict
        Diccionario con la información del primer sector vial.
    s2 : dict
        Diccionario con la información del segundo sector vial.
    s3 : dict
        Diccionario con la información del tercer sector vial.
    s4 : dict
        Diccionario con la información del cuarto sector vial.

    Retorno
    -------
    dict
        Diccionario que tiene como llaves el nombre del sitio especial y como
        valores la cantidad de sitios especiales que existen de ese sitio.
        Las llaves deben ser "zona_recreacional", "cuello_de_botella" y
        "zona_escolar"

    """
    diccionario_con_suma_sitios_especiales = {
        "zona_recreacional": 0,
        "cuello_de_botella": 0, 
        "zona_escolar": 0
        }

    diccionario_con_suma_sitios_especiales["zona_recreacional"] += zonas_recreativas("zona_recreacional", s1)
    diccionario_con_suma_sitios_especiales["cuello_de_botella"] += zonas_recreativas("cuello_de_botella", s1)
    diccionario_con_suma_sitios_especiales["zona_escolar"] += zonas_recreativas("zona_escolar", s1)

    diccionario_con_suma_sitios_especiales["zona_recreacional"] += zonas_recreativas("zona_recreacional", s2)
    diccionario_con_suma_sitios_especiales["cuello_de_botella"] += zonas_recreativas("cuello_de_botella", s2)
    diccionario_con_suma_sitios_especiales["zona_escolar"] += zonas_recreativas("zona_escolar", s2)

    diccionario_con_suma_sitios_especiales["zona_recreacional"] += zonas_recreativas("zona_recreacional", s3)
    diccionario_con_suma_sitios_especiales["cuello_de_botella"] += zonas_recreativas("cuello_de_botella", s3)
    diccionario_con_suma_sitios_especiales["zona_escolar"] += zonas_recreativas("zona_escolar", s3)

    diccionario_con_suma_sitios_especiales["zona_recreacional"] += zonas_recreativas("zona_recreacional", s4)
    diccionario_con_suma_sitios_especiales["cuello_de_botella"] += zonas_recreativas("cuello_de_botella", s4)
    diccionario_con_suma_sitios_especiales["zona_escolar"] += zonas_recreativas("zona_escolar", s4)

    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return diccionario_con_suma_sitios_especiales


def zonas_recreativas(zona: str, seccion: dict) -> str:
    """
    Dice si tiene la zona recreativa solicitada.

    Parámetros
    ----------
    seccion : dict
        Diccionario con la información del  sector vial.


    Retorno
    -------
    int
       retorna 1 si la zona es una zona recreativa, de lo contrario retorna 0. 

    """
    if seccion.get(zona) == True:
        return 1
    else:
        return 0

