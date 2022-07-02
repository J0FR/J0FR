"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

from gettext import Catalog
import config as cf
import model
import csv
import timeit
from DISClib.ADT import map as mp
import datetime

from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import graph as gr
from DISClib.DataStructures import mapentry as me




import sys
sys.setrecursionlimit(10000000)


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog


def loadRoutes(catalog, routesFile):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.
    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    routesFile = cf.data_dir + routesFile
    input_file = csv.DictReader(open(routesFile, encoding="utf-8"),
                                delimiter=",")
    fila_incorrecta = 0
    contador = 0
    first_five = lt.newList(datastructure="ARRAY_LIST")
    last_five = lt.newList(datastructure="ARRAY_LIST")
    for ruta in input_file:
        contador += 1
        if ruta["Bike Id"] == "" \
            or int(ruta["Trip  Duration"]) <= 0 \
            or ruta["Trip  Duration"] == "" \
            or ruta["Start Station Id"] == "" \
            or ruta["End Station Id"] == "" \
            or ruta["Start Station Name"] == ruta["End Station Name"]:
            fila_incorrecta += 1 
            continue
        else:
            if lt.size(first_five) != 5:
                lt.addLast(first_five, ruta)
                lt.addFirst(last_five, ruta)
            else:
                lt.addLast(last_five, ruta)
                lt.removeFirst(last_five)
            ruta['Start Time Parcial'] = datetime.datetime.strptime(ruta['Start Time'][0:10], '%m/%d/%Y')
            ruta['End Time Parcial'] = datetime.datetime.strptime(ruta['End Time'][0:10], '%m/%d/%Y')
            ruta['Start Time Hora'] = datetime.datetime.strptime(ruta['Start Time'][0:13], '%m/%d/%Y %H')
            ruta['End Time Hora'] = datetime.datetime.strptime(ruta['End Time'][0:13], '%m/%d/%Y %H')
            ruta['Start Time'] = datetime.datetime.strptime(ruta['Start Time'], '%m/%d/%Y %H:%M')
            ruta['End Time'] = datetime.datetime.strptime(ruta['End Time'], '%m/%d/%Y %H:%M')
            ruta['NombreForStart'] = ruta['Start Station Id']+"-"+ruta["Start Station Name"]
            ruta['NombreForEnd'] = ruta['End Station Id']+"-"+ruta["End Station Name"]
            model.Viaje(catalog, ruta)
    model.Viaje.aniadir_conexiones(catalog)
    catalog["filas_incorrectas"] = fila_incorrecta

    catalog["respuesta_req3"] = model.grafo_scc(catalog)

    catalog["first_five"] = first_five
    catalog["last_five"] = last_five


    model.Estacion.respuesta_req1(catalog)
    
    
    return catalog
    

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def grafo_dijsktra(catalog, vertice_inicial):
    return model.grafo_dijsktra(catalog, vertice_inicial)

def hasPath(catalog, station_to_reach):
    return model.hasPath(catalog, station_to_reach)

def findPath(catalog, station_to_reach):
    return model.findPath(catalog, station_to_reach)

def mayorCantidad_salidas(catalog, lst):
    return model.mayorCantidad_salidas(catalog, lst)


def mayorCantidad_llegadas(catalog, lst):
    return model.mayorCantidad_llegadas(catalog, lst)

def requerimiento1(catalog):
    return catalog["respuesta_req1"]

def requerimiento3(catalog):
    return model.formatear_respuesta_req3(catalog, )

def requirement4(analyzer, origin_station, arrival_station):
    return model.requirement4(analyzer, origin_station, arrival_station)

def requerimiento5(catalog, fecha_inicial, fecha_final):
    return model.Viaje.respuesta_req5(catalog, fecha_inicial, fecha_final)

def requerimiento6(catalog, id_bici):
    return model.Bicicleta.respuesta_req6(catalog, id_bici)

def requerimiento_2(catalog, initialVertex, maxDuration, numMinStopStations, maxStations):
    return model.posibles_rutas_de_viaje(catalog, initialVertex, maxDuration, numMinStopStations, maxStations)


# djikstra

def minimumCostPaths(catalog, initialStation):
    return model.minimumCostPaths(catalog, initialStation)

def hasPath(catalog, destStation):
    return model.hasPath(catalog, destStation)

def minimumCostPath(catalog, destStation):
    return model.minimumCostPath(catalog, destStation)

def req4(catalog, estacion_inicial, estacion_final):
    return model.req4(catalog, estacion_inicial, estacion_final)

def req_bono(obj, estacion, fechaInicial, fechaFinal):
    return model.Estacion.respuesta_reqBono(obj, estacion, fechaInicial, fechaFinal)

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo


def requerimiento_2(catalog, initialVertex, maxDuration, numMinStopStations, maxStations):
    return model.posibles_rutas_de_viaje(catalog, initialVertex, maxDuration, numMinStopStations, maxStations)




def clearConsole():
    model.clearConsole()

def exitProgram():
    model.exitProgram()