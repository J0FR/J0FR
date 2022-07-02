"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from prettytable import PrettyTable
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
from DISClib.Algorithms.Graphs import scc
import model




"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    """
    Funcion encargada de hacer mostrar en la consola las opciones del menu
    """       
    print("Bienvenido")
    print("1- Comprar bicicletas para las estaciones con mas viajes de origen - Requerimiento 1")
    print("2- Planear paseos turisticos por la ciudad - Requerimiento 2")
    print("3- Reconocer los componentes fuertemente conectados - Requerimiento 3")
    print("4- Planear una ruta rapida para el usuario - Requerimiento 4")
    print("5- Reportar rutas en un rango de fechas para los usuarios anuales - Requerimiento 5")
    print("6- Planear el mantenimiento preventivo de bicicletas - Requerimiento 6")
    print("7- La estacion mas frecuentada por los visitantes - Requerimiento 7")
    print("8- Cargar información en el catálogo")



"""
 - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว -

        Funciones para mostrar en la consola los datos solicitados

 - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว - (งツ)ว -
"""

def print_req1(catalog, numero_estaciones, response):
    print("===================== Req No. 1 Inputs =====================")
    print("TOP 5 stations inside in the Bikeshre Network.")
    print(f"Number of stations in the network: {numero_estaciones}")

    print("===================== Req No. 1 Answer =====================")
    print("TOP 5 stations used as trip origins are:")
    table = PrettyTable()
    table.field_names = ["Station ID", "Station Name", "Out Trips", "Subscriber Out Trips", "Turist Out Trips", "Out Degree (Routes)", "Rush hour", "Rush date"]
    table.max_table_width = 120
    table.max_width = 20
    for _ in lt.iterator(response):
        table.add_row([me.getValue(mp.get(_, "id_estacion")),
                        me.getValue(mp.get(_, "nombre")),
                        me.getValue(mp.get(_, "trayectos_iniciados")),
                        me.getValue(mp.get(_, "numero_subscriptorAnual")),
                        me.getValue(mp.get(_, "numero_turistas")),
                        gr.outdegree(catalog["grafo"], f'{me.getValue(mp.get(_, "id_estacion"))}-{me.getValue(mp.get(_, "nombre"))}'),
                        f"{me.getValue(mp.get(_, 'max_hora'))}:00h",
                        f"01/01/{me.getValue(mp.get(_, 'max_anio'))}"
                        ])
    print(table.get_string())

def printRequerimiento2(routes, size, estacion_origen, maxDuration, numMinStopsStations, maxStations):
    print("================== Req No. 2 Inputs ==================")
    print(f"Available time: '{maxDuration}' [sec]")
    print()
    print(f"Minimum number of Stations '{numMinStopsStations}'")
    print()
    print(f"Maximum number of routes: '{maxStations}'")
    print()
    print("================== Req No. 2 Answer ==================")
    print()
    print(f"From {estacion_origen} are {size} possible routes")
    table = PrettyTable()
    table.field_names = ["Stops Stations", "Route Time ", "Start Stations", "Stop Stations"]
    table.max_table_width = 120
    table.max_width = 20
    for _ in range(1,6):
        for i in lt.iterator(routes):
                path = i[1]
                stop_stations = lt.size(i[1]) + 1
                info = {}
                w = []
                i = []
                f = []
                for station in lt.iterator(path):
                    weight = station[0]
                    initial_station = station[1]
                    finish_station = station[2]
                    w.append(weight)
                    i.append(initial_station)
                    f.append(finish_station)
                    info["weight"] = round(sum(w),2)
                    info["initial_station"] = i
                    info["finish_station"] = f
                table.add_row([stop_stations,
                                info["weight"],
                                info["initial_station"],
                                info["finish_station"]])
    return print(table.get_string())

def print_req3(catalog, respuesta):
    print("===================== Req No. 3 Inputs =====================")
    print("+++ Calculating the strongly connected components +++")
    print("...")
    print()
    print("===================== Req No. 3 Answer =====================")
    print(f"There are {scc.connectedComponents(catalog['grafo_scc'])} Strongly connected components (SCC) in the graph.")
    print()
    print(f" +++ The SCC details are: +++ ")
    print(f"The first 3 and last 3 of the SCC are:")
    cantidad_elementos = scc.connectedComponents(catalog['grafo_scc'])

    lst = lt.getElement(respuesta, 1)
    size = lt.size(lst) -2 
    componente = lt.getElement(lst, 1)
    obj_out = controller.mayorCantidad_salidas(catalog, lst)
    obj_in = controller.mayorCantidad_llegadas(catalog, lst)
    print(f"SCC size: {size}")
    print(f"SCCID: {componente}")
    print(f"Max out station ID: {obj_out.id_estacion}")
    print(f"Max out station name: {obj_out.nombre}")
    print(f"Max in station ID: {obj_in.id_estacion}")
    print(f"Max in station name: {obj_in.nombre}")
    print()

    lst = lt.getElement(respuesta, 3)
    size = lt.size(lst) -2
    componente = lt.getElement(lst, 1)
    obj_out = controller.mayorCantidad_salidas(catalog, lst)
    obj_in = controller.mayorCantidad_llegadas(catalog, lst)
    print(f"SCC size: {size}")
    print(f"SCCID: {componente}")
    print(f"Max out station ID: {obj_out.id_estacion}")
    print(f"Max out station name: {obj_out.nombre}")
    print(f"Max in station ID: {obj_in.id_estacion}")
    print(f"Max in station name: {obj_in.nombre}")
    print()

    lst = lt.getElement(respuesta, 5)
    size = lt.size(lst)-2
    componente = lt.getElement(lst, 1)
    obj_out = controller.mayorCantidad_salidas(catalog, lst)
    obj_in = controller.mayorCantidad_llegadas(catalog, lst)
    print(f"SCC size: {size}")
    print(f"SCCID: {componente}")
    print(f"Max out station ID: {obj_out.id_estacion}")
    print(f"Max out station name: {obj_out.nombre}")
    print(f"Max in station ID: {obj_in.id_estacion}")
    print(f"Max in station name: {obj_in.nombre}")
    print()

    lst = lt.getElement(respuesta, cantidad_elementos - 2)
    size = lt.size(lst)-2
    componente = lt.getElement(lst, 1)
    obj_out = controller.mayorCantidad_salidas(catalog, lst)
    obj_in = controller.mayorCantidad_llegadas(catalog, lst)
    print(f"SCC size: {size}")
    print(f"SCCID: {componente}")
    print(f"Max out station ID: {obj_out.id_estacion}")
    print(f"Max out station name: {obj_out.nombre}")
    print(f"Max in station ID: {obj_in.id_estacion}")
    print(f"Max in station name: {obj_in.nombre}")
    print()

    lst = lt.getElement(respuesta, cantidad_elementos - 1)
    size = lt.size(lst)-2
    componente = lt.getElement(lst, 1)
    obj_out = controller.mayorCantidad_salidas(catalog, lst)
    obj_in = controller.mayorCantidad_llegadas(catalog, lst)
    print(f"SCC size: {size}")
    print(f"SCCID: {componente}")
    print(f"Max out station ID: {obj_out.id_estacion}")
    print(f"Max out station name: {obj_out.nombre}")
    print(f"Max in station ID: {obj_in.id_estacion}")
    print(f"Max in station name: {obj_in.nombre}")
    print()

    lst = lt.getElement(respuesta, cantidad_elementos)
    size = lt.size(lst)-2
    componente = lt.getElement(lst, 1)
    obj_out = controller.mayorCantidad_salidas(catalog, lst)
    obj_in = controller.mayorCantidad_llegadas(catalog, lst)
    print(f"SCC size: {size}")
    print(f"SCCID: {componente}")
    print(f"Max out station ID: {obj_out.id_estacion}")
    print(f"Max out station name: {obj_out.nombre}")
    print(f"Max in station ID: {obj_in.id_estacion}")
    print(f"Max in station name: {obj_in.nombre}")
    print()

    print("=========== ACA ACABA ==============")


def print_req5(respuesta):
    totalViajesRealizados = respuesta[0]
    totalTiempoViajes = respuesta[1]
    estacionDeOrigenMasFrecuentadaid = respuesta[2]
    estacionDeOrigenMasFrecuentada = respuesta[3]
    estacionDeDestinoMasFrecuentadaid = respuesta[4]
    estacionDeDestinoMasFrecuentada = respuesta[5]
    horaDiaMasViajesInician = respuesta[6]
    horaDiaMasViajesTerminan = respuesta[7]
    print("===================== Req No. 5 Inputs =====================")
    print("+++ Calculating the strongly connected components +++")
    print("...")
    print()
    print("===================== Req No. 5 Answer =====================")
    print(f"Total viajes realizados: {totalViajesRealizados}")
    print(f"El total de tiempo invertido en los viajes: {totalTiempoViajes} segundos")
    print(f"La estación de origen más frecuentada: {estacionDeOrigenMasFrecuentadaid} - {estacionDeOrigenMasFrecuentada}")
    print(f"La estación de destino más utilizada: {estacionDeDestinoMasFrecuentadaid} - {estacionDeDestinoMasFrecuentada}")
    print(f"La hora del día en la que más viajes inician {horaDiaMasViajesInician}:00h")
    print(f"La hora del día en la que más viajes terminan: {horaDiaMasViajesTerminan}:00h")
    print()

def print_req6(respuesta, id_bici):
    print("===================== Req No. 6 Inputs =====================")
    print(f"+++ Analize trips with the bike ID {id_bici} +++")
    print()
    print("===================== Req No. 6 Answer =====================")
    total_viajes = me.getValue(mp.get(respuesta, "total_viajes"))
    horas_de_uso = me.getValue(mp.get(respuesta, "horas_de_uso"))
    estacionIniciado_mas_viajes = me.getValue(mp.get(respuesta, "estacionIniciado_mas_viajes"))
    estacionIniciado_mas_viajes = lt.getElement(estacionIniciado_mas_viajes, 1).split("-")
    estacionFinalizado_mas_viajes = me.getValue(mp.get(respuesta, "estacionFinalizado_mas_viajes"))
    estacionFinalizado_mas_viajes = lt.getElement(estacionFinalizado_mas_viajes, 1).split("-")
    print(f"El total de viajes en los que ha participado dicha bicicleta: {total_viajes}")
    print(f"El total de horas de utilización de la bicicleta: {horas_de_uso}")
    print(f"La estación en la que más viajes se han iniciado en esa bicicleta: {estacionIniciado_mas_viajes[1]} con id {estacionIniciado_mas_viajes[0]}")
    print(f"La estación en la que más viajes ha terminado dicha bicicleta: {estacionFinalizado_mas_viajes[1]} con id {estacionFinalizado_mas_viajes[0]}")
    print()

def print_req4(estacion_inicio, estacion_final, costo, path):
    print("===================== Req No. 4 Inputs =====================")
    print(f"Camino de {estacion_inicio} a {estacion_final}")
    print()
    print("===================== Req No. 4 Answer =====================")
    print(f"Este recorrido tiene un costo de: {costo} segundos")
    print()
    print("El camino esta formado de la siguiente forma")
    contador = 1
    for _ in lt.iterator(path):
        print(f"Paso #{contador}")
        vertexA = _['vertexA'].split("-")
        vertexB = _['vertexB'].split("-")
        print(f"Sale de la estacion {vertexA[1]} con id {vertexA[0]}")
        print(f"Llega a la estacion {vertexB[1]} con id {vertexB[0]}")
        print(f"Este recorrido tendra un tiempo promedio de {_['weight']} segundos")
        print()
        contador += 1
    
def print_req7(respuesta):
    inicia = lt.getElement(respuesta[2], 1)
    termina = lt.getElement(respuesta[2], 2)
    print("=== Bono ===")
    print(f"El total de viajes que iniciaron en dicha estación en el rango de tiempo solicitado: {inicia}")
    print(f"El total de viajes que terminaron en dicha estación en el rango de tiempo solicitado: {termina}")
    print(f"El viaje de mayor duración promedio saliendo de la estación de consulta: {respuesta[0]}")
    print(f"La estación donde terminaron la mayoría de los viajes que iniciaron en la estación: {respuesta[1]}")


def seleccionar_estacion(catalog, estacion):
    lst_estacion = me.getValue(mp.get(catalog['nombreEstaciones_nombreFormateados'], estacion))
    if lt.size(lst_estacion) > 1:
        contador = 1
        for _ in lt.iterator(lst_estacion):
            print(f"Opcion {contador}: {_}")
            contador += 1
        opcion = input(f"Cual desearia escoger? (1-{contador})")
        estacion = lt.getElement(lst_estacion, opcion)
    else:
        estacion = lt.getElement(lst_estacion, 1)
    return estacion


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    # Condicional para seleccionar la opcion 1 (Comprar bicicletas para las estaciones con mas viajes de origen)
    if int(inputs[0]) == 1:
        response = controller.requerimiento1(catalog)
        print_req1(catalog, catalog["numero_de_estaciones"], response)
        
    # Condicional para seleccionar la opcion 2 (Planear paseos turisticos por la ciudad)
    elif int(inputs[0]) == 2:
        estacion_origen = input("Ingrese el nombre de la estacion de la cual quiere partir: ")
        estacion_origen = seleccionar_estacion(catalog, estacion_origen)
        maxDuration = int(input("Ingrese cual es el maximo de tiempo del recorrido: "))
        numMinStopsStations = int(input("Ingrese la cantidad de estaciones que quiere visitar: "))
        maxStations = int(input("Ingrese el maximo de paradas que quiere hacer: "))
        routes, size = controller.requerimiento_2(catalog, estacion_origen, maxDuration, numMinStopsStations, maxStations)
        printRequerimiento2(routes, size, estacion_origen,maxDuration, numMinStopsStations, maxStations )

    # Condicional para seleccionar la opcion 3 (Reconocer los componentes fuertemente conectados)
    elif int(inputs[0]) == 3:
        respuesta = catalog["respuesta_req3"]
        print_req3(catalog, respuesta)
    
    # Condicional para seleccionar la opcion 4 (Planear una ruta rapida para el usuario) 
    elif int(inputs[0]) == 4:
        estacion_origen = input("Desde donde deseas que salga el usuario: ")
        estacion_origen = seleccionar_estacion(catalog, estacion_origen)
        estacion_destino = input("A donde desea llegar el usuario: ")
        estacion_destino = seleccionar_estacion(catalog, estacion_destino)


        path, costo = controller.req4(catalog, estacion_origen, estacion_destino)
        print_req4(estacion_origen, estacion_destino, costo, path)
        
    # Condicional para seleccionar la opcion 5 (Reportar rutas en un rango de fechas para los usuarios anuales)
    elif int(inputs[0]) == 5:
        fecha_inicial = input("Por favor ingrese la fecha inicial: ")
        fecha_final = input("Por favor ingrese la fecha final: ")
        respuesta = controller.requerimiento5(catalog, fecha_inicial, fecha_final)

        print_req5(respuesta)

    # Condicional para seleccionar la opcion 6 (Planear el mantenimiento preventivo de bicicletas)
    elif int(inputs[0]) == 6:
        id_bici = input("Por favor ingrese el id de la bici: ")
        respuesta = controller.requerimiento6(catalog, id_bici)
        print_req6(respuesta, id_bici)
#Sherbourne St / Wellesley St E

    elif int(inputs[0]) == 7:
        nombre_estacion = input("Nombre de la estación: ")
        nombre_estacion = seleccionar_estacion(catalog, nombre_estacion)
        obj = me.getValue(mp.get(catalog['estaciones'], nombre_estacion))
        fecha_inicio = input("Fecha y hora de inicio: ")
        fecha_final = input("Fecha y hora de finalización: ")
        respuesta = controller.req_bono(obj, nombre_estacion, fecha_inicio, fecha_final)

        
        print_req7(respuesta)
    # Condicional para seleccionar la opcion 8 (Cargar información en el catálogo)
    elif int(inputs[0]) == 8:
        # avance carga datos
        import time
        print("Cargando información de los archivos ....")
        catalog = controller.init()

        start_time = time.time()
        catalog = controller.loadRoutes(catalog, "Bikeshare-ridership-2021-utf8-small.csv")
        print("--- %s seconds ---" % (time.time() - start_time))
        from DISClib.ADT import graph as gr
        print(f"El total de viajes obtenidos de los datos: {model.Viaje.cantidad_viajes}")
        print(f"Numero de vertices en el grafo: {gr.numVertices(catalog['grafo'])}")
        print(f"Numero de arcos en el grafo: {gr.numEdges(catalog['grafo'])}")
        for _ in lt.iterator(catalog["first_five"]):
            obj = me.getValue(mp.get(catalog['estaciones'], _['Start Station Id']+'-'+_['Start Station Name']))
            print(f"Station ID: {_['Start Station Id']}")
            print(f"Station name: {_['Start Station Name']}")
            print(f"Indegree: {gr.indegree(catalog['grafo'], obj.nombre_formatedo)}")
            print(f"Outdegree: {gr.outdegree(catalog['grafo'], obj.nombre_formatedo)}")
            print(f"In trips: {obj.estacion_llegada}")
            print(f"Out trips: {obj.estacion_salida}")
            print()
        for _ in lt.iterator(catalog["last_five"]):
            obj = me.getValue(mp.get(catalog['estaciones'], _['Start Station Id']+'-'+_['Start Station Name']))
            print(f"Station ID: {_['Start Station Id']}")
            print(f"Station name: {_['Start Station Name']}")
            print(f"Indegree: {gr.indegree(catalog['grafo'], obj.nombre_formatedo)}")
            print(f"Outdegree: {gr.outdegree(catalog['grafo'], obj.nombre_formatedo)}")
            print(f"In trips: {obj.estacion_llegada}")
            print(f"Out trips: {obj.estacion_salida}")
            print()


    else:
        sys.exit(0)
sys.exit(0)
