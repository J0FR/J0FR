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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from re import L
import config as cf
from DISClib.ADT import graph as gr
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import stack as st
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import scc
from DISClib.ADT import orderedmap as om
from DISClib.Utils import error as error
assert cf
import datetime
import os



import sys
sys.setrecursionlimit(10000000)



"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el analizador
   stops: Tabla de hash para guardar los vertices del grafo
   connections: Grafo para representar las rutas entre estaciones
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        catalog = {
            'grafo': None,
            'grafo_scc': None,
            'maxValue_stationInComponent': None,
            'peso_arcos': None,
            'paths': None,
            'componentesFuertementeConectados': None,
        }

        catalog['estaciones'] = mp.newMap(numelements=14000, maptype='PROBING', loadfactor=0.5)        

        catalog['nombreEstaciones_nombreFormateados'] = mp.newMap(numelements=14000, maptype='PROBING', loadfactor=0.5)   

        catalog['idBicicleta_objetoBicicleta'] = mp.newMap(numelements=14000, maptype='PROBING', loadfactor=0.5)   

        catalog['grafo'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareStopIds)
        catalog["componentesFuertementeConectados"] = lt.newList(datastructure='ARRAY_LIST')

        catalog["arbolFechas_viajes_usuariosAnuales"] = om.newMap(comparefunction=compare_generalArboles)

        catalog["respuesta_req3"] = None

        catalog["respuesta_req1"] = None

        catalog["numero_de_estaciones"] = None


        return catalog
    except Exception as exp:
        error.reraise(exp, 'model:newCatalog')


def grafo_scc(catalog):
    grafo = catalog["grafo"]
    lst_componentes = catalog["componentesFuertementeConectados"]
    catalog["grafo_scc"] = scc.KosarajuSCC(grafo)
    scc_ = catalog["grafo_scc"]

    numero_de_componentesFuertementementeConectados = scc.connectedComponents(scc_)
    value = scc.sccCount(grafo, scc_, "7543-Nassau St / Bellevue Ave")['idscc']

    estacion = mp.keySet(value)
    componente = mp.valueSet(value)
    cantidad = lt.size(estacion)

    for _ in range(1, numero_de_componentesFuertementementeConectados + 1):
        lst = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lst, _)
        lt.addLast(lst_componentes, lst)
    

    for _ in range(1, cantidad + 1):
        estation = lt.getElement(estacion, _)
        comp = lt.getElement(componente, _)
        lst_actual = lt.getElement(lst_componentes, comp)
        lt.addLast(lst_actual, estation)

    lst_componentes = sa.sort(lst_componentes, cmpGeneral2)
    
    return lst_componentes

def formatear_respuesta_req3(catalog, firstThree, lastThree):
    lst_respuesta = lt.newList(datastructure='ARRAY_LIST')
    for _ in lt.iterator(firstThree):
        size = lt.size(_) - 1
        lst_respuestaActual = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lst_respuestaActual, lt.getElement(_, 1))
        lt.addLast(lst_respuestaActual, size)
        resSalidas = mayorCantidad_salidas(catalog, _)
        resLlegadas = mayorCantidad_llegadas(catalog, _)
        lt.addLast(lst_respuestaActual, resSalidas)
        lt.addLast(lst_respuestaActual, resLlegadas)
        lt.addLast(lst_respuesta, lst_respuestaActual)
    for _ in lt.iterator(lastThree):
        size = lt.size(_) - 1
        lst_respuestaActual = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lst_respuestaActual, lt.getElement(_, 1))
        lt.addLast(lst_respuestaActual, size)
        resSalidas = mayorCantidad_salidas(catalog, _)
        resLlegadas = mayorCantidad_llegadas(catalog, _)
        lt.addLast(lst_respuestaActual, resSalidas)
        lt.addLast(lst_respuestaActual, resLlegadas)
        lt.addLast(lst_respuesta, lst_respuestaActual)
    catalog["respuesta_req3"] = lst_respuesta
    return lst_respuesta

def mayorCantidad_salidas(catalog, lst):
    mapa_estaciones = catalog['estaciones']
    
    max = -1
    estacion = None
    for element in lt.iterator(lst):
        if isinstance(element, int):
            continue
        object = me.getValue(mp.get(mapa_estaciones, element))
        salidas = object.estacion_salida
        if salidas > max:
            max = salidas
            estacion = object
    return estacion

def mayorCantidad_llegadas(catalog, lst):
    mapa_estaciones = catalog['estaciones']
    
    max = -1
    estacion = None
    for element in lt.iterator(lst):
        if isinstance(element, int):
            continue
        object = me.getValue(mp.get(mapa_estaciones, element))
        llegadas = object.estacion_llegada
        if llegadas > max:
            max = llegadas
            estacion = object
    return estacion









def minimumCostPaths(catalog, initialStation):
    """
    Calcula los caminos de costo mínimo desde la estacion initialStation
    a todos los demas vertices del grafo
    """
    catalog['paths'] = djk.Dijkstra(catalog['grafo'], initialStation)
    return catalog['paths']


def hasPath(catalog, destStation):
    """
    Indica si existe un camino desde la estacion inicial a la estación destino
    Se debe ejecutar primero la funcion minimumCostPaths
    """
    return djk.hasPathTo(catalog['paths'], destStation)


def minimumCostPath(catalog, destStation):
    """
    Retorna el camino de costo minimo entre la estacion de inicio
    y la estacion destino
    Se debe ejecutar primero la funcion minimumCostPaths
    """
    path = djk.pathTo(catalog['paths'], destStation)
    return path


def req4(catalog, estacion_inicial, estacion_final):
    grafo_dijsktra = minimumCostPaths(catalog, estacion_inicial)
    existe = djk.hasPathTo(grafo_dijsktra, estacion_final)
    if existe:
        costo = djk.distTo(grafo_dijsktra, estacion_final)
        path = minimumCostPath(catalog, estacion_final)
        return path, costo
    else:
        return "No hay camino"



def compareStopIds(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1

def cmpGeneral(val1, val2):
    val1 = lt.getElement(val1, 1)
    val2 = lt.getElement(val2, 1)
    return val1 > val2

def cmpGeneral2(val1, val2):
    val_1 = lt.size(val1)
    val_2 = lt.size(val2)
    val_ = lt.getElement(val1, 1)
    val2_ = lt.getElement(val2, 1)
    if val_1 == val_2:
        return val_ > val2_
    else:
        return val_1 > val_2

def cmpGeneral3(val1, val2):
    val1 = lt.getElement(val1, 2)
    val2 = lt.getElement(val2, 2)
    return val1 > val2

def compare_generalArboles(val1, val2):
    if (val1 == val2):
        return 0
    elif val1 > val2:
        return 1
    else:
        return -1



# Modelos de los objetos 

class Estacion:

    cantidad_estaciones = 0
    top_estacionesSalida = lt.newList(datastructure='ARRAY_LIST')
    mapa_reqBono = mp.newMap()

    def __init__(self, nombre_formateado, nombre, id_estacion) -> None:
        self.nombre = nombre
        self.nombre_formatedo = nombre_formateado
        self.id_estacion = id_estacion
        self.estacion_numSalida = lt.newList(datastructure='ARRAY_LIST')
        
        lt.addLast(self.estacion_numSalida, 0)
        lt.addLast(self.estacion_numSalida, self.nombre_formatedo)
        lt.addLast(Estacion.top_estacionesSalida, self.estacion_numSalida)
        
        self.mayor_duracion_promedio_viaje = -1
        self.estacion_terminaron = mp.newMap(numelements=29, maptype='PROBING', loadfactor=0.5)

        self.estacion_llegada = 0
        self.estacion_salida = 0
        self.estacion_salidaTuristas = 0
        self.estacion_salidaSubscriptores = 0
        self.registro_hora = mp.newMap(numelements=29, maptype='PROBING', loadfactor=0.5)
        self.registro_anio = mp.newMap(numelements=29, maptype='PROBING', loadfactor=0.5)
        self.arcos = mp.newMap(numelements=5, maptype='PROBING', loadfactor=0.5)

        Estacion.cantidad_estaciones += 1
    
    def mayor_duracion(self, duracion):
        if self.mayor_duracion_promedio_viaje < int(duracion):
            self.mayor_duracion_promedio_viaje = int(duracion)
    
    def aniadir_llegada(self) -> None:
        self.estacion_llegada += 1
    
    def aniadir_salida(self, nombreFormateado_estacionLlegada, peso_de_estacion, hora, subscripcion):
        self.mayor_duracion(peso_de_estacion)
        self.registrar_hora(hora)
        self.registrar_anio(hora)
        self.estacion_salida += 1
        if subscripcion == "Casual Member":
            self.estacion_salidaTuristas += 1
        if subscripcion == "Annual Member":
            self.estacion_salidaSubscriptores += 1
        
        peso_de_estacion = float(peso_de_estacion)
        
        mapa = self.arcos

        existe_estacion = mp.contains(mapa, nombreFormateado_estacionLlegada)

        val = lt.getElement(self.estacion_numSalida, 1)
        lt.changeInfo(self.estacion_numSalida, 1, val + 1)

        if existe_estacion:
            peso = mp.get(mapa, nombreFormateado_estacionLlegada)
            lst_peso = me.getValue(peso)
            cantidad_elementos = lt.getElement(lst_peso, 1)
            peso = lt.getElement(lst_peso, 2)

            lt.changeInfo(lst_peso, 1, cantidad_elementos + 1)
            lt.changeInfo(lst_peso, 2, peso + peso_de_estacion)

        else:
            lst = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lst, 1)
            lt.addLast(lst, peso_de_estacion)
            mp.put(mapa, nombreFormateado_estacionLlegada, lst)
    
    def registrar_hora(self, datetime):
        mapa = self.registro_hora
        hour = datetime.hour
        existe = mp.contains(mapa, hour)
        if existe:
            val = me.getValue(mp.get(mapa, hour))
            mp.put(mapa, hour, val + 1)
        else:
            mp.put(mapa, hour, 1)
    
    def registrar_anio(self, datetime):
        mapa = self.registro_anio
        anio = datetime.year
        existe = mp.contains(mapa, anio)
        if existe:
            val = me.getValue(mp.get(mapa, anio))
            mp.put(mapa, anio, val + 1)
        else:
            mp.put(mapa, anio, 1)
    
    def registrar_estacion_terminaron(self, estacion):
        mapa = self.estacion_terminaron
        existe = mp.contains(mapa, estacion)
        if existe:
            val = me.getValue(mp.get(mapa, estacion))
            mp.put(mapa, estacion, val + 1)
        else:
            mp.put(mapa, estacion, 1)
    
    # Requerimiento bono
    def hallar_estacion_donde_llegaron_mayor_cantidad_de_viajes(self):
        mapa = self.estacion_terminaron
        keys = mp.keySet(mapa)
        maximo = -1 
        for _ in lt.iterator(keys):
            value = me.getValue(mp.get(mapa, _))
            if value > maximo:
                maximo = value
        return maximo
    
    def total_viajes_queIniciaronYTerminaronEnRango(self, estacion, fechaInicial, fechaFinal):
        mapa = Estacion.mapa_reqBono
        fechaInicial = datetime.datetime.strptime(fechaInicial, '%m/%d/%Y %H')
        fechaFinal = datetime.datetime.strptime(fechaFinal, '%m/%d/%Y %H')
        mapa = me.getValue(mp.get(mapa, estacion))
        valores = om.values(mapa, fechaInicial, fechaFinal)

        respuesta = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(respuesta, 0)
        lt.addLast(respuesta, 0)
        for _ in lt.iterator(valores):
            current_value1 = lt.getElement(respuesta, 1)
            current_value2 = lt.getElement(respuesta, 2)
            value_inicia = lt.getElement(_, 1)
            value_termina = lt.getElement(_, 2)
            lt.changeInfo(respuesta, 1, current_value1 + value_inicia)
            lt.changeInfo(respuesta, 2, current_value2 + value_termina)

        return respuesta

    def respuesta_reqBono(self, estacion, fechaInicial, fechaFinal):
        max_IniciaTermina = self.total_viajes_queIniciaronYTerminaronEnRango(estacion, fechaInicial, fechaFinal)
        maximo = self.hallar_estacion_donde_llegaron_mayor_cantidad_de_viajes
        return (self.mayor_duracion_promedio_viaje, maximo, max_IniciaTermina)


    
    def respuesta_req1(catalog):
        lst = lt.newList()
        res = sa.sort(Estacion.top_estacionesSalida, cmpGeneral)
        mapa = catalog['estaciones']
        res = lt.subList(res, 1, 5)
        for _ in lt.iterator(res):
            new_mapa = mp.newMap()
            city_name = lt.getElement(_, 2)
            objeto = me.getValue(mp.get(mapa, city_name))
            mp.put(new_mapa, "nombre", objeto.nombre)
            mp.put(new_mapa, "id_estacion", objeto.id_estacion)
            mp.put(new_mapa, "trayectos_iniciados", objeto.estacion_salida)
            mp.put(new_mapa, "numero_subscriptorAnual", objeto.estacion_salidaSubscriptores)
            mp.put(new_mapa, "numero_turistas", objeto.estacion_salidaTuristas)
            max_hora = lt.newList()
            lt.addLast(max_hora, -1)
            lt.addLast(max_hora, -1)
            mapa_horas = objeto.registro_hora
            llaves_horas = mp.keySet(objeto.registro_hora)
            max_anio = lt.newList()
            lt.addLast(max_anio, -1)
            lt.addLast(max_anio, -1)
            mapa_anios = objeto.registro_anio
            llaves_anios = mp.keySet(objeto.registro_anio)
            for hora in lt.iterator(llaves_horas):
                val = me.getValue(mp.get(mapa_horas, hora))
                val_lst = lt.getElement(max_hora, 2)
                if val_lst < val:
                    lt.changeInfo(max_hora, 2, val)
                    lt.changeInfo(max_hora, 1, hora)
            
            for anio in lt.iterator(llaves_anios):
                val = me.getValue(mp.get(mapa_anios, anio))
                val_lst = lt.getElement(max_anio, 2)
                if val_lst < val:
                    lt.changeInfo(max_anio, 2, val)
                    lt.changeInfo(max_anio, 1, anio)
            
            mp.put(new_mapa, "max_anio", lt.getElement(max_anio, 1))
            mp.put(new_mapa, "max_hora", lt.getElement(max_hora, 1))
            lt.addLast(lst, new_mapa)

        catalog["respuesta_req1"] = lst


class Bicicleta:
    total_bicicletas = 0
    def __init__(self, id) -> None:
        Bicicleta.total_bicicletas += 1
        self.id_bicicleta = id
        self.tiempo_de_uso_bicicleta = 0
        self.total_viajes = 0

        self.estaciones_iniciado = lt.newList(datastructure="ARRAY_LIST")
        self.estaciones_iniciadoMapa = mp.newMap(numelements=29, maptype='PROBING', loadfactor=0.5)
        self.estaciones_terminado = lt.newList(datastructure="ARRAY_LIST")
        self.estaciones_terminadoMapa = mp.newMap(numelements=29, maptype='PROBING', loadfactor=0.5)

    def anidir_uso(self, duracion):
        self.tiempo_de_uso_bicicleta += duracion
    
    def aniadir_estacionInicio(self, estacion, duracion):
        self.total_viajes += 1
        self.anidir_uso(int(duracion))
        existe = mp.contains(self.estaciones_iniciadoMapa, estacion)
        if existe:
            lst = me.getValue(mp.get(self.estaciones_iniciadoMapa, estacion))
            val = lt.getElement(lst, 2)
            lt.changeInfo(lst, 2, val + 1)
        else:
            lst = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lst, estacion)
            lt.addLast(lst, 1)
            lt.addLast(self.estaciones_iniciado, lst)
            mp.put(self.estaciones_iniciadoMapa, estacion, lst)
            
    
    def aniadir_estacionFinalizacion(self, estacion):
        existe = mp.contains(self.estaciones_terminadoMapa, estacion)
        if existe:
            lst = me.getValue(mp.get(self.estaciones_terminadoMapa, estacion))
            val = lt.getElement(lst, 2)
            lt.changeInfo(lst, 2, val + 1)
        else:
            lst = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lst, estacion)
            lt.addLast(lst, 1)
            lt.addLast(self.estaciones_terminado, lst)
            mp.put(self.estaciones_terminadoMapa, estacion, lst)
    
    def sort(self):
        sa.sort(self.estaciones_iniciado, cmpGeneral3)
        sa.sort(self.estaciones_terminado, cmpGeneral3)
    
    def respuesta_req6(catalog, id_bici):
        bici = me.getValue(mp.get(catalog['idBicicleta_objetoBicicleta'], id_bici))
        mapa = mp.newMap()
        mp.put(mapa, "total_viajes", bici.total_viajes)
        mp.put(mapa, "horas_de_uso", bici.tiempo_de_uso_bicicleta/3600)
        mp.put(mapa, "estacionIniciado_mas_viajes", lt.getElement(bici.estaciones_iniciado, 1))
        mp.put(mapa, "estacionFinalizado_mas_viajes", lt.getElement(bici.estaciones_terminado, 1))
        return mapa







class Viaje:

    cantidad_viajes = 0
    

    def __init__(self, catalog, route) -> None:
        Viaje.cantidad_viajes += 1


        self.id_viaje = Viaje.cantidad_viajes
        self.nombre_estacionSalida = route['Start Station Name']
        self.id_estacionSalida = route["Start Station Id"]
        self.nombreFormateado_estacionSalida = self.formatear_nombre(self.id_estacionSalida, self.nombre_estacionSalida)

        self.nombre_estacionLlegada = route['End Station Name']
        self.id_estacionLlegada = route["End Station Id"].split('.')[0]
        self.nombreFormateado_estacionLlegada = self.formatear_nombre(self.id_estacionLlegada, self.nombre_estacionLlegada)

        self.peso = route["Trip  Duration"]

        
        if route["User Type"] == "Annual Member":
            self.aniadirFecha_arbol(catalog, route, self.nombreFormateado_estacionSalida, self.nombreFormateado_estacionLlegada)
        else:
            Viaje.requerimiento_bono_iniciaron(route)

        # Datos bicicleta
        id = route["Bike Id"]
        idBicicleta_objetoBicicleta = catalog['idBicicleta_objetoBicicleta']
        existe = mp.contains(idBicicleta_objetoBicicleta, id)
        if existe:
            bicicleta = me.getValue(mp.get(idBicicleta_objetoBicicleta, id))
            bicicleta.aniadir_estacionInicio(self.nombreFormateado_estacionSalida, route["Trip  Duration"])
            bicicleta.aniadir_estacionFinalizacion(self.nombreFormateado_estacionLlegada)
        else:
            bicicleta = Bicicleta(id)
            bicicleta.aniadir_estacionInicio(self.nombreFormateado_estacionSalida, route["Trip  Duration"])
            bicicleta.aniadir_estacionFinalizacion(self.nombreFormateado_estacionLlegada)
            mp.put(idBicicleta_objetoBicicleta, id, bicicleta)
        Bicicleta.sort

        mapa_estaciones = catalog['estaciones']
        nombreEstaciones_nombreFormateados = catalog['nombreEstaciones_nombreFormateados']
        grafo = catalog['grafo']
        fecha_salida = route["Start Time"]
        subscripcion = route["User Type"]
        self.agregar_datosViaje(grafo, mapa_estaciones, self.nombreFormateado_estacionSalida, self.nombre_estacionSalida, self.id_estacionSalida, self.nombreFormateado_estacionLlegada, self.peso, nombreEstaciones_nombreFormateados, self.nombre_estacionLlegada, self.id_estacionLlegada, fecha_salida, subscripcion)
    
    def agregar_datosViaje(self,
                            grafo,
                            mapa_estaciones,
                            nombreFormateado_estacionSalida,
                            nombre_estacionSalida, id_estacionSalida,
                            nombreFormateado_estacionLlegada,
                            peso,
                            nombreEstaciones_nombreFormateados,
                            nombre_estacionLlegada,
                            id_estacionLlegada,
                            hora_salida, subscripcion):

        self.salida(grafo, mapa_estaciones, nombreFormateado_estacionSalida, nombre_estacionSalida, id_estacionSalida, nombreFormateado_estacionLlegada, peso, nombreEstaciones_nombreFormateados, hora_salida, subscripcion)
        self.llegada(grafo, mapa_estaciones, nombreFormateado_estacionLlegada, nombre_estacionLlegada, id_estacionLlegada, nombreEstaciones_nombreFormateados)
    
    def formatear_nombre(self, id, nombre) -> str:
        return f"{id}-{'UNKNOWN' if nombre == '' else nombre}"

    def salida(self, grafo, mapa_estaciones, nombreFormateado_estacionSalida, nombre_estacionSalida, id_estacionSalida, nombreFormateado_estacionLlegada, peso, nombreEstaciones_nombreFormateados, hora_salida, subscripcion):
        self.aniadirNombreEstacion_estacionFormateada(nombreEstaciones_nombreFormateados, nombre_estacionSalida, nombreFormateado_estacionSalida)
        contiene_llave = mp.contains(mapa_estaciones, nombreFormateado_estacionSalida)
    
        if contiene_llave:
            estacion = me.getValue(mp.get(mapa_estaciones, nombreFormateado_estacionSalida))
            estacion.aniadir_salida(nombreFormateado_estacionLlegada, peso, hora_salida, subscripcion)
        else:
            estacion = Estacion(nombreFormateado_estacionSalida, nombre_estacionSalida, id_estacionSalida)
            estacion.aniadir_salida(nombreFormateado_estacionLlegada, peso, hora_salida, subscripcion)
            mp.put(mapa_estaciones, nombreFormateado_estacionSalida, estacion)
            gr.insertVertex(grafo, nombreFormateado_estacionSalida)


    def llegada(self, grafo, mapa_estaciones, nombreFormateado_estacionLlegada, nombre_estacionLlegada, id_estacionLlegada, nombreEstaciones_nombreFormateados):
        self.aniadirNombreEstacion_estacionFormateada(nombreEstaciones_nombreFormateados, nombre_estacionLlegada, nombreFormateado_estacionLlegada)
        contiene_llave = mp.contains(mapa_estaciones, nombreFormateado_estacionLlegada)

        if contiene_llave:
            estacion = me.getValue(mp.get(mapa_estaciones, nombreFormateado_estacionLlegada))
            estacion.aniadir_llegada()
        else:
            estacion = Estacion(nombreFormateado_estacionLlegada, nombre_estacionLlegada, id_estacionLlegada)
            estacion.aniadir_llegada()
            mp.put(mapa_estaciones, nombreFormateado_estacionLlegada, estacion)
            gr.insertVertex(grafo, nombreFormateado_estacionLlegada)
        
    def aniadirNombreEstacion_estacionFormateada(self, mapa, nombre_estacion, nombreFormateado_estacion):
        existe = mp.contains(mapa, nombre_estacion)
        if existe:
            lst = me.getValue(mp.get(mapa, nombre_estacion))
            existe = lt.isPresent(lst, nombreFormateado_estacion)
            if not existe:
                lt.addLast(lst, nombreFormateado_estacion)
        else:
            lst = lt.newList()
            mp.put(mapa, nombre_estacion, lst)
            lt.addLast(lst, nombreFormateado_estacion)
    
    def aniadir_conexiones(catalog):
        mapa_estaciones = catalog['estaciones']
        grafo = catalog['grafo']

        nombre_estaciones = mp.keySet(mapa_estaciones)
        for estacion in lt.iterator(nombre_estaciones):
            valor = me.getValue(mp.get(mapa_estaciones, estacion))
            arcos = valor.arcos
            nombre_estacionesSalida = mp.keySet(arcos)
            for estacionSalida in lt.iterator(nombre_estacionesSalida):
                lst_peso = me.getValue(mp.get(arcos, estacionSalida))
                gr.addEdge(grafo, estacion, estacionSalida, lt.getElement(lst_peso, 2) / lt.getElement(lst_peso, 1))
    
    
    def aniadirFecha_arbol(self, catalog, route, nombreFormateado_estacionSalida, nombreFormateado_estacionLlegada):
        arbol = catalog["arbolFechas_viajes_usuariosAnuales"]
        fecha1 = route["Start Time"]
        fecha2 = route["End Time"]
        fechaParcial1 = route["Start Time Parcial"]
        fechaParcial2 = route["End Time Parcial"]
        
        existe1 = om.contains(arbol, fechaParcial1)
        existe2 = om.contains(arbol, fechaParcial2)

        tiempo_viaje = int(route["Trip  Duration"])
        dia1 = fecha1.day
        dia2 = fecha2.day
        hora1 = int(fecha1.hour)
        hora2 = int(fecha2.hour)
        
        if dia1 == dia2:
            if existe1:
                lst = me.getValue(om.get(arbol, fechaParcial1))
                mapa_estacionOrigen = lt.getElement(lst, 3)
                mapa_estacionDestino = lt.getElement(lst, 4)
                mapa_horasOrigen= lt.getElement(lst, 5)
                mapa_horasDestino= lt.getElement(lst, 6)
                
                val_totalViajes = lt.getElement(lst, 1)
                val_totalTiempoViaje = lt.getElement(lst, 2)
                
                try:
                    veces_estacionOrigen = me.getValue(mp.get(mapa_estacionOrigen, nombreFormateado_estacionSalida))
                    mp.put(mapa_estacionOrigen, nombreFormateado_estacionSalida, veces_estacionOrigen + 1)
                except:
                    mp.put(mapa_estacionOrigen, nombreFormateado_estacionSalida, 1)
                
                try:
                    veces_estacionDestino = me.getValue(mp.get(mapa_estacionDestino, nombreFormateado_estacionLlegada))
                    mp.put(mapa_estacionDestino, nombreFormateado_estacionLlegada, veces_estacionDestino + 1)
                except:
                    mp.put(mapa_estacionDestino, nombreFormateado_estacionLlegada, 1)

                veces_horaOrigen = me.getValue(mp.get(mapa_horasOrigen, hora1))
                veces_horaDestino = me.getValue(mp.get(mapa_horasDestino, hora2))


                mp.put(mapa_horasOrigen, hora1, veces_horaOrigen + 1)
                mp.put(mapa_horasDestino, hora2, veces_horaDestino + 1)

                lt.changeInfo(lst, 1, val_totalViajes + 1)
                lt.changeInfo(lst, 2, val_totalTiempoViaje + tiempo_viaje)
                lt.changeInfo(lst, 3, mapa_estacionOrigen)
                lt.changeInfo(lst, 4, mapa_estacionDestino)
                lt.changeInfo(lst, 5, mapa_horasOrigen)
                lt.changeInfo(lst, 6, mapa_horasDestino)
                om.put(arbol, fechaParcial1, lst)
            else:
                lst = lt.newList(datastructure='ARRAY_LIST')
                mapa_estacionOrigen = mp.newMap()
                mapa_estacionDestino = mp.newMap()
                mapa_horasOrigen= mp.newMap()
                mapa_horasDestino= mp.newMap()
                mp.put(mapa_estacionOrigen, nombreFormateado_estacionSalida, 1)
                mp.put(mapa_estacionDestino, nombreFormateado_estacionLlegada, 1)
                for _ in range(24):
                    mp.put(mapa_horasOrigen, _, 0)
                    mp.put(mapa_horasDestino, _, 0)
                mp.put(mapa_horasOrigen, hora1, 1)
                mp.put(mapa_horasDestino, hora2, 1)
                lt.addLast(lst, 1)
                lt.addLast(lst, tiempo_viaje)
                lt.addLast(lst, mapa_estacionOrigen)
                lt.addLast(lst, mapa_estacionDestino)
                lt.addLast(lst, mapa_horasOrigen)
                lt.addLast(lst, mapa_horasDestino)
                om.put(arbol, fechaParcial1, lst)

        else:
            if existe1:
                lst = me.getValue(om.get(arbol, fechaParcial1))
                mapa_estacionOrigen = lt.getElement(lst, 3)
                mapa_horasOrigen= lt.getElement(lst, 5)
                val_totalViajes = lt.getElement(lst, 1)
                val_totalTiempoViaje = lt.getElement(lst, 2)
                lt.changeInfo(lst, 1, val_totalViajes + 1)
                lt.changeInfo(lst, 2, val_totalTiempoViaje + tiempo_viaje)
                
                try:
                    veces_estacionOrigen = me.getValue(mp.get(mapa_estacionOrigen, nombreFormateado_estacionSalida))
                    mp.put(mapa_estacionOrigen, nombreFormateado_estacionSalida, veces_estacionOrigen + 1)
                except:
                    mp.put(mapa_estacionOrigen, nombreFormateado_estacionSalida, 1)

                veces_horaOrigen = me.getValue(mp.get(mapa_horasOrigen, hora1))
                mp.put(mapa_horasOrigen, hora1, veces_horaOrigen + 1)

                lt.changeInfo(lst, 1, val_totalViajes + 1)
                lt.changeInfo(lst, 2, val_totalTiempoViaje + tiempo_viaje)
                lt.changeInfo(lst, 3, mapa_estacionOrigen)
                lt.changeInfo(lst, 5, mapa_horasOrigen)
                om.put(arbol, fechaParcial1, lst)                

            else:
                lst = lt.newList(datastructure='ARRAY_LIST')
                mapa_estacionOrigen = mp.newMap()
                mapa_estacionDestino = mp.newMap()
                mapa_horasOrigen= mp.newMap()
                mapa_horasDestino= mp.newMap()
                mp.put(mapa_estacionOrigen, nombreFormateado_estacionSalida, 1)
                for _ in range(24):
                    mp.put(mapa_horasOrigen, _, 0)
                    mp.put(mapa_horasDestino, _, 0)
                mp.put(mapa_horasOrigen, hora1, 1)
                lt.addLast(lst, 1)
                lt.addLast(lst, tiempo_viaje)
                lt.addLast(lst, mapa_estacionOrigen)
                lt.addLast(lst, mapa_estacionDestino)
                lt.addLast(lst, mapa_horasOrigen)
                lt.addLast(lst, mapa_horasDestino)
                om.put(arbol, fechaParcial1, lst)

            if existe2:
                lst = me.getValue(om.get(arbol, fechaParcial2))
                val_totalViajes = lt.getElement(lst, 1)
                val_totalTiempoViaje = lt.getElement(lst, 2)
                mapa_estacionDestino = lt.getElement(lst, 4)
                mapa_horasDestino= lt.getElement(lst, 6)

                

                try:
                    veces_estacionDestino = me.getValue(mp.get(mapa_estacionDestino, nombreFormateado_estacionLlegada))
                    mp.put(mapa_estacionDestino, nombreFormateado_estacionLlegada, veces_estacionDestino + 1)
                except:
                    mp.put(mapa_estacionDestino, nombreFormateado_estacionLlegada, 1)
                
                veces_horaDestino = me.getValue(mp.get(mapa_horasDestino, hora2))
                mp.put(mapa_horasDestino, hora2, veces_horaDestino + 1)

                lt.changeInfo(lst, 1, val_totalViajes + 1)
                lt.changeInfo(lst, 2, val_totalTiempoViaje + tiempo_viaje)
                lt.changeInfo(lst, 4, mapa_estacionDestino)
                lt.changeInfo(lst, 6, mapa_horasDestino)
                om.put(arbol, fechaParcial2, lst)
            else:
                lst = lt.newList(datastructure='ARRAY_LIST')
                mapa_estacionOrigen = mp.newMap()
                mapa_estacionDestino = mp.newMap()
                mapa_horasOrigen= mp.newMap()
                mapa_horasDestino= mp.newMap()
                mp.put(mapa_estacionDestino, nombreFormateado_estacionLlegada, 1)
                for _ in range(24):
                    mp.put(mapa_horasOrigen, _, 0)
                    mp.put(mapa_horasDestino, _, 0)
                mp.put(mapa_horasDestino, hora2, 1)
                lt.addLast(lst, 1)
                lt.addLast(lst, tiempo_viaje)
                lt.addLast(lst, mapa_estacionOrigen)
                lt.addLast(lst, mapa_estacionDestino)
                lt.addLast(lst, mapa_horasOrigen)
                lt.addLast(lst, mapa_horasDestino)
                om.put(arbol, fechaParcial2, lst)
    
    def respuesta_req5(catalog, fecha_inicial, fecha_final):
        mapa = catalog["arbolFechas_viajes_usuariosAnuales"]
        fecha_inicial = datetime.datetime.strptime(fecha_inicial, '%m/%d/%Y')
        fecha_final = datetime.datetime.strptime(fecha_final, '%m/%d/%Y')
        valores = om.values(mapa, fecha_inicial, fecha_final)

        estacionOrigenMasFrecuentada = lt.newList()
        estacionOrigenMasFrecuentada_mapa = mp.newMap()
        estacionDestinoMasFrecuentada = lt.newList()
        estacionDestinoMasFrecuentada_mapa = mp.newMap()
        horaDelDiaMasViajesInician = lt.newList()
        horaDelDiaMasViajesInician_mapa = mp.newMap()
        horaDelDiaMasViajesTerminan = lt.newList()
        horaDelDiaMasViajesTerminan_mapa = mp.newMap()

        # cmpGeneral3 - elemento a comparar 2

        totalViajesRealizados = 0
        totalTiempoViajes = 0
        for dia in lt.iterator(valores):
            totalViajesRealizados += lt.getElement(dia, 1)
            totalTiempoViajes += lt.getElement(dia, 2)
            mapa_estacionOrigen = lt.getElement(dia, 3)
            mapa_estacionDestino = lt.getElement(dia, 4)
            mapa_horasOrigen = lt.getElement(dia, 5)
            mapa_horasDestino = lt.getElement(dia, 6)
            
            # loop mapa_estacionOrigen
            keys = mp.keySet(mapa_estacionOrigen)
            for key in lt.iterator(keys):
                existe = mp.contains(estacionOrigenMasFrecuentada_mapa, key)
                if existe:
                    value_lst = me.getValue(mp.get(estacionOrigenMasFrecuentada_mapa, key))
                    info = lt.getElement(value_lst, 2)
                    lt.changeInfo(value_lst, 2, info + me.getValue(mp.get(mapa_estacionOrigen, key)))
                else:
                    lst = lt.newList()
                    lt.addLast(lst, key)
                    lt.addLast(lst, me.getValue(mp.get(mapa_estacionOrigen, key)))
                    lt.addLast(estacionOrigenMasFrecuentada, lst)
                    mp.put(estacionOrigenMasFrecuentada_mapa, key, lst)
            
            keys = mp.keySet(mapa_estacionDestino)
            for key in lt.iterator(keys):
                existe = mp.contains(estacionDestinoMasFrecuentada_mapa, key)
                if existe:
                    value_lst = me.getValue(mp.get(estacionDestinoMasFrecuentada_mapa, key))
                    info = lt.getElement(value_lst, 2)
                    lt.changeInfo(value_lst, 2, info + me.getValue(mp.get(mapa_estacionDestino, key)))
                else:
                    lst = lt.newList()
                    lt.addLast(lst, key)
                    lt.addLast(lst, me.getValue(mp.get(mapa_estacionDestino, key)))
                    lt.addLast(estacionDestinoMasFrecuentada, lst)
                    mp.put(estacionDestinoMasFrecuentada_mapa, key, lst)

            keys = mp.keySet(mapa_horasOrigen)
            for key in lt.iterator(keys):
                existe = mp.contains(horaDelDiaMasViajesInician_mapa, key)
                if existe:
                    value_lst = me.getValue(mp.get(horaDelDiaMasViajesInician_mapa, key))
                    info = lt.getElement(value_lst, 2)
                    lt.changeInfo(value_lst, 2, info + me.getValue(mp.get(mapa_horasOrigen, key)))
                else:
                    lst = lt.newList()
                    lt.addLast(lst, key)
                    lt.addLast(lst, me.getValue(mp.get(mapa_horasOrigen, key)))
                    lt.addLast(horaDelDiaMasViajesInician, lst)
                    mp.put(horaDelDiaMasViajesInician_mapa, key, lst)

            keys = mp.keySet(mapa_horasDestino)
            for key in lt.iterator(keys):
                existe = mp.contains(horaDelDiaMasViajesTerminan_mapa, key)
                if existe:
                    value_lst = me.getValue(mp.get(horaDelDiaMasViajesTerminan_mapa, key))
                    info = lt.getElement(value_lst, 2)
                    lt.changeInfo(value_lst, 2, info + me.getValue(mp.get(mapa_horasDestino, key)))
                else:
                    lst = lt.newList()
                    lt.addLast(lst, key)
                    lt.addLast(lst, me.getValue(mp.get(mapa_horasDestino, key)))
                    lt.addLast(horaDelDiaMasViajesTerminan, lst)
                    mp.put(horaDelDiaMasViajesTerminan_mapa, key, lst)
            
        sa.sort(estacionOrigenMasFrecuentada, cmpGeneral3)
        sa.sort(estacionDestinoMasFrecuentada, cmpGeneral3)
        sa.sort(horaDelDiaMasViajesInician, cmpGeneral3)
        sa.sort(horaDelDiaMasViajesTerminan, cmpGeneral3)

        estacionDeOrigenMasFrecuentada = lt.getElement(estacionOrigenMasFrecuentada, 1)
        estacionDeDestinoMasFrecuentada = lt.getElement(estacionDestinoMasFrecuentada, 1)
        horaDiaMasViajesInician = lt.getElement(horaDelDiaMasViajesInician, 1)
        horaDiaMasViajesTerminan= lt.getElement(horaDelDiaMasViajesTerminan, 1)

        return (totalViajesRealizados, totalTiempoViajes, lt.getElement(estacionDeOrigenMasFrecuentada, 1), lt.getElement(estacionDeOrigenMasFrecuentada, 2), lt.getElement(estacionDeDestinoMasFrecuentada, 1), lt.getElement(estacionDeDestinoMasFrecuentada, 2), lt.getElement(horaDiaMasViajesInician, 1), lt.getElement(horaDiaMasViajesTerminan, 1))

    def requerimiento_bono_iniciaron(route):
        mapa = Estacion.mapa_reqBono
        date = route["Start Time Hora"]
        endDate = route["End Time Hora"]
        existe = mp.contains(mapa, route['NombreForStart'] )
        existe2 = mp.contains(mapa, route['NombreForEnd'])
        if not existe:
            new_orderMap = om.newMap(omaptype="RBT", comparefunction=compare_generalArboles)
            lst = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lst, 1)
            lt.addLast(lst, 0)
            om.put(new_orderMap, date, lst)
            mp.put(mapa, route['NombreForStart'] , new_orderMap)
        if not existe2:
            new_orderMap = om.newMap(omaptype="RBT", comparefunction=compare_generalArboles)
            lst = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lst, 0)
            lt.addLast(lst, 1)
            om.put(new_orderMap, endDate, lst)
            mp.put(mapa, route['NombreForEnd'], new_orderMap)
            
        valueStart = me.getValue(mp.get(mapa, route['NombreForStart'] )) 
        mapa_om1 = om.contains(valueStart, date)      
        if mapa_om1:
            lst = me.getValue(om.get(valueStart, date))
            
            lt.changeInfo(lst, 1, lt.getElement(lst, 1) + 1)
        else:
            lst = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lst, 0)
            lt.addLast(lst, 1)
            om.put(valueStart, date, lst)

        valueEnd = me.getValue(mp.get(mapa, route['NombreForEnd']))   
        mapa_om1 = om.contains(valueEnd, endDate)      
        if mapa_om1:
            lst = me.getValue(om.get(valueEnd, endDate))
            
            lt.changeInfo(lst, 1, lt.getElement(lst, 1) + 1)
        else:
            lst = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lst, 0)
            lt.addLast(lst, 1)
            om.put(valueEnd, endDate, lst)       

        
#=========================

                
# =========================
# Funciones para consola
# =========================
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def exitProgram():
    os._exit(1)


def minimumCostPath(analyzer, destStation):
    """
    Retorna el camino de costo minimo entre la estacion de inicio
    y la estacion destino
    Se debe ejecutar primero la funcion minimumCostPaths
    """
    path = djk.pathTo(analyzer['paths'], destStation)
    return path

def posibles_rutas_de_viaje(catalog, initialVertex, maxDuration, numMinStopStations, maxStations):

    #id_station = mp.get(catalog['nombreEstaciones_nombreFormateados'], initialVertex)
    #initialVertex = me.getValue(id_station)

    dij = minimumCostPaths(catalog, initialVertex)
    visited = dij["visited"]
    stations = mp.keySet(visited)
    trip_duration = maxDuration / 2
    routes = lt.newList('ARRAY_LIST')

    for i in lt.iterator(stations):
        duration = djk.distTo(dij, i)
        path = djk.pathTo(dij, i)

        if path is not None:
            cantidad_estaciones = st.size(path)
            if duration <= trip_duration and numMinStopStations <= cantidad_estaciones:
                lt.addLast(routes, path)

    user_routes = lt.subList(routes, 1, maxStations)
    list_paths = lt.newList('ARRAY_LIST')

    for route in lt.iterator(user_routes):
        list_path = lt.newList('ARRAY_LIST')
        conteo = 0


        while (not st.isEmpty(route)):
            stop = st.pop(route)
            station_info = (stop['weight'], stop['vertexA'], stop['vertexB'])
            lt.addLast(list_path, station_info)
            conteo += stop['weight']

        path_info = (conteo, list_path)
        lt.addLast(list_paths, path_info)

    return list_paths, lt.size(routes)




# los que llegan asi mismo y los que no tienen duracion (o los que tienen duracion 0)