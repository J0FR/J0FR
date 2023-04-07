"""
Ejercicio nivel 2: Cálculo de velocidades en vías colombianas
Modulo de interacción por consola.

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

import calculadora_de_velocidades as mod


def mostrar_sector( sector: dict ) -> None:
    """
    Muestra en pantalla las características de un sector vial de la vía.

    Parámetros
    ----------
    sector : dict
        Diccionario del sector vial a mostrar.

    """
    
    nombre = sector["nombre"]
    carriles = sector["carriles"]
    pendiente = sector["pendiente"]
    ancho_calzada = sector["ancho_calzada"]
    ancho_berma = sector["ancho_berma"]
    separador = sector["separador"]
    peatones = sector["peatones"]
    accesos = sector["control_accesos"]
    recreacional = sector["zona_recreacional"]
    cuello_botella = sector["cuello_de_botella"]
    zona_escolar = sector["zona_escolar"]

    print("Nombre: " + nombre + 
          "\n\nCaracterísticas geométricas\n" +
          "\nCarriles: " + str(carriles) + " - Pendiente: " + str(pendiente) +
          "\nAncho calzada: " + str(ancho_calzada) + " m - Ancho berma: "
          + str(ancho_berma) + " m" +
          "\n\nSeparadores, peatones y tipo de accesos controlados\n" +
          "\nTiene separador: " + str(separador) + 
          "\nTiene concentración de peatones: " + str(peatones) +
          "\nTipo de accessos controlados: " + str(accesos) + 
          "\n\nSitios especiales\n" +
          "\nTiene zona recreacional: " + str(recreacional) +
          "\nTiene cuello de botella: " + str(cuello_botella) + 
          "\nTiene zona escolar: " + str(zona_escolar))


def ejecutar_clasificar_sector( s1: dict, s2: dict, s3: dict,
                               s4: dict ) -> None:
    """
    Ejecuta la función que clasifica un sector vial según sus características
    geométricas.

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

    El programa debe mostrar al usuario: "El sector vial es de tipo XX.", en el
    cual XX es alguno de los 7 posibles tipos de clasificación según
    características geométricas.

    """
    #TODO: Completar
    nombre = input("Ingrese el nombre del sector que quiere buscar: ")
    buscar_sector = mod.buscar_sector(nombre, s1, s2, s3, s4)

    #TODO: Completar
    print(f"El sector vial es de tipo {mod.clasificar_sector(buscar_sector)}")


def ejecutar_velocidad_generica( s1: dict, s2: dict, s3: dict,
                                s4: dict ) -> None:
    """
    Ejecuta la función que determina la velocidad genérica de un sector.

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

    El programa debe mostrar al usuario: "La velocidad genérica del sector YYY
    es de XXX km/h.", en el que YYY es el nombre del sector y XXX la velocidad
    genérica del sector en kilómetros por hora.

    """
    #TODO: Completar
    nombre = input("Ingrese el nombre del sector que quiere buscar: ")
    buscar_sector = mod.buscar_sector(nombre, s1, s2, s3, s4)
    print(f"La velocidad genérica del sector {nombre} es de {mod.determinar_velocidad_generica(buscar_sector)} km/h.")



def ejecutar_velocidad_promedio( s1: dict, s2: dict, s3: dict,
                                s4: dict ) -> None:
    """
    Ejecuta la función que calcula la velocidad promedio de un sector teniendo
    en cuenta sus restricciones por sitios especiales.

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

    El programa debe mostrar al usuario: "La velocidad promedio del sector YYY
    es de XXX km/h.", en el que YYY es el nombre del sector y XXX la velocidad
    promedio del sector en kilómetros por hora.

    """
    nombre = input("Ingrese el nombre del sector que quiere buscar: ")
    buscar_sector = mod.buscar_sector(nombre, s1, s2, s3, s4)
    print(f"La velocidad promedio del sector {nombre} es de {mod.calcular_velocidad_promedio(buscar_sector)} km/h.")
    #TODO: Completar


def ejecutar_contar_libres_de_restriccion( s1: dict, s2: dict, s3: dict,
                                          s4: dict ) -> None:
    """
    Ejecuta la función que cuenta cuántos los sectores que no tienen sitios
    especiales.

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

    El programa debe mostrar al usuario: "El número de sectores que no tienen
    sitios especiales es: X.", en el que X es la cantidad de sectores sin 
    sitios especiales.

    """
    print(f"El número de sectores que no tienen sitios especiales es: {mod.contar_libres_de_restriccion(s1, s2, s3, s4)}.")

    #TODO: Completar


def ejecutar_pendiente_menor( s1: dict, s2: dict, s3: dict, s4: dict ) -> None:
    """
    Ejecuta la función que muestra los sectores con una pendiente menor a una
    indicada por el usuario.

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

    El programa debe mostrar al usuario: "Los sectores con pendiente menor a
    X son: YYY.", en el que X es la pendiente ingresada por el usuario y YYY 
    son los sectores que tienen una pendiente menor a la ingresada.
    """
    #TODO: Completar
    pendiente = float(input("Ingrese la cota superior para la pendiente: "))
    print(f"Los sectores con pendiente menor a {pendiente} son: {mod.determinar_pendiente_menor(pendiente, s1, s2, s3, s4)}.")


def ejecutar_velocidad_maxima( s1: dict, s2: dict, s3: dict,
                              s4: dict ) -> None:
    """
    Ejecuta la función que encuentra el sector con la máxima velocidad 
    genérica. En caso de haber sectores con la misma velocidad, se debe 
    mostrar el nombre del sector que vaya primero alfabéticamente.

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

    El programa debe mostrar al usuario: "El sector con la máxima velocidad
    genérica es el sector YYY.", en el que YYY es el nombre del sector con la
    máxima velocidad genérica.

    """
    dic_sec_vel_mas_alta = mod.velocidad_maxima(s1, s2, s3, s4)
    nombre = dic_sec_vel_mas_alta["nombre"]
    velocidad_generica = mod.determinar_velocidad_generica(dic_sec_vel_mas_alta)
    print(f"El sector con la máxima velocidad genérica mas alta es el sector {nombre} - {velocidad_generica}km/h.")
    # TODO: Completar


def ejecutar_contar_sitios_especiales( s1: dict, s2: dict, s3: dict,
                                      s4: dict ) -> None:
    """
    Ejecuta la función que cuenta los sitios especiales de todos los sectores.

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

    El programa debe mostrar al usuario: "Hay X zonas recreacionales, Y 
    cuellos de botella y Z zonas escolares en todos los sectores de la vía."

    """
    diccionario_sitios_especiales = mod.contar_sitios_especiales(s1, s2, s3, s4)
    zona_recreacional = diccionario_sitios_especiales["zona_recreacional"]
    cuello_de_botella = diccionario_sitios_especiales["cuello_de_botella"]
    zona_escolar = diccionario_sitios_especiales["zona_escolar"]
    print(f"Hay {zona_recreacional} zonas recreacionales, {cuello_de_botella} cuellos de botella y {zona_escolar} zonas escolares en todos los sectores de la vía.")
    #TODO: Completar


def iniciar_aplicacion():
    """
    Inicia la ejecución de la aplicacion por consola.
    Esta función primero crea cuatro sectores de la vía Cartagena-Macondo.
    Luego la función le muestra el menú al usuario y espera a que seleccione
    una opción. Esta operación se repite hasta que el usuario seleccione la
    opción de salir.
    
    """
    sector1 = mod.crear_sector("Melquíades", 4, 0.03, 7.3, 2.5,True, False,
                               "Total",False, False, False)
    sector2 = mod.crear_sector("Remedios", 4, 0.05, 7.3, 1.5, True, False,
                               "Parcial", False, True, True)
    sector3 = mod.crear_sector("Crespi", 3, 0.045, 7.3, 1.5, False, False,
                               "Nulo", True, True, False)
    sector4 = mod.crear_sector("Buendía", 2, 0.06, 7.3, 1.8, False, True,
                               "Nulo", True, True, False)

    ejecutando = True
    while ejecutando:
        print("\n\nSectores de la vía Cartagena-Macondo\n" + ("-"*50))
        print("Sector 1\n")
        mostrar_sector(sector1)
        print("-"*50)

        print("Sector 2\n")
        mostrar_sector(sector2)
        print("-"*50)

        print("Sector 3\n")
        mostrar_sector(sector3)
        print("-"*50)

        print("Sector 4\n")
        mostrar_sector(sector4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(sector1, sector2, sector3, sector4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion( s1: dict, s2: dict, s3: dict, s4: dict ) -> bool:
    """
    Le muestra al usuario las opciones de ejecución disponibles.

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
    bool
        Esta función retorna True si el usuario seleccionó una opción
        diferente a la opción que le permite salir de la aplicación.
        Esta función retorna False si el usuario seleccionó la opción para
        salir de la aplicación.

    """
    print("Menu de opciones")
    print(" 1 - Clasificar según características geométricas")
    print(" 2 - Determinar velocidad genérica")
    print(" 3 - Determinar velocidad promedio")
    print(" 4 - Contar sectores sin sitios especiales")
    print(" 5 - Sectores con pendiente menor a un valor")
    print(" 6 - Velocidad genérica más alta")
    print(" 7 - Contar sitios especiales")
    print(" 8 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_clasificar_sector(s1, s2, s3, s4)
    elif opcion_elegida == "2":
        ejecutar_velocidad_generica(s1, s2, s3, s4)
    elif opcion_elegida == "3":
        ejecutar_velocidad_promedio(s1, s2, s3, s4)
    elif opcion_elegida == "4":
        ejecutar_contar_libres_de_restriccion(s1, s2, s3, s4)
    elif opcion_elegida == "5":
        ejecutar_pendiente_menor(s1, s2, s3, s4)
    elif opcion_elegida == "6":
        ejecutar_velocidad_maxima(s1, s2, s3, s4)
    elif opcion_elegida == "7":
        ejecutar_contar_sitios_especiales(s1, s2, s3, s4)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción valida.")
    return continuar_ejecutando


iniciar_aplicacion()

