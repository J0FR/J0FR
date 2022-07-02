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

import config as cf
import model
import csv
import tracemalloc
import time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# ===========================
# Inicialización del Catálogo
# ===========================

def newCatalog():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# ================================
# Funciones para la carga de datos
# ================================

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    tracemalloc.start()

    start_time = getTime()
    start_memory = getMemory()

    FirstThreeAlbums, LastThreeAlbums = CargaAlbums(catalog)
    FirstThreeArtists, LastThreeArtists = CargaArtists(catalog)
    FirstThreeTracks, LastThreeTracks = CargaTracks(catalog)

    stop_memory = getMemory()
    stop_time = getTime()

    tracemalloc.stop()

    delta_time = deltaTime(stop_time, start_time)
    delta_memory = deltaMemory(stop_memory, start_memory)

    sizeAlbums = model.sizeMap(catalog['model']['albums_id'])
    sizeArtists = model.sizeMap(catalog['model']['artists_id'])
    sizeTracks = model.sizeMap(catalog['model']['tracks_id'])

    return delta_time, delta_memory, sizeAlbums, sizeArtists, sizeTracks, FirstThreeAlbums, LastThreeAlbums, FirstThreeArtists, LastThreeArtists, FirstThreeTracks, LastThreeTracks


def CargaAlbums(catalog):
    """
    Carga los libros del archivo. Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    albums = cf.data_dir + 'spotify-albums-utf8-small.csv'
    input_file = csv.DictReader(open(albums, encoding='utf-8'))
    FirstThreeAlbums = model.newList("ARRAY_LIST")
    LastThreeAlbums = model.newList("SINGLE_LINKED")
    for album in input_file:
        model.cargaAlbum(catalog['model'], album)
        model.getFirstAndLastThree(album, FirstThreeAlbums, LastThreeAlbums)
    return FirstThreeAlbums, LastThreeAlbums
        


def CargaArtists(catalog):
    """
    Carga los libros del archivo. Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    artists = cf.data_dir + 'spotify-artists-utf8-small.csv'
    input_file = csv.DictReader(open(artists, encoding='utf-8'))
    FirstThreeArtists = model.newList("ARRAY_LIST")
    LastThreeArtists = model.newList("SINGLE_LINKED")
    for artist in input_file:
        model.cargaArtists(catalog['model'], artist)
        model.getFirstAndLastThree(artist, FirstThreeArtists, LastThreeArtists)
    return FirstThreeArtists, LastThreeArtists


def CargaTracks(catalog):
    """
    Carga los libros del archivo. Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    tracks = cf.data_dir + 'spotify-tracks-utf8-small.csv'
    input_file = csv.DictReader(open(tracks, encoding='utf-8'))
    FirstThreeTracks = model.newList("ARRAY_LIST")
    LastThreeTracks = model.newList("SINGLE_LINKED")
    for track in input_file:
        model.cargaTracks(catalog['model'], track)
        model.getFirstAndLastThree(track, FirstThreeTracks, LastThreeTracks)
    return FirstThreeTracks, LastThreeTracks



# =========================
# Funciones de ordenamiento
# ==========================




# =====================
# Funciones de consulta
# =====================

def artistID_to_artistName(catalog, artist_id):
    return model.artistID_to_artistName(catalog, artist_id)

def trackID_to_trackName(catalog, track_id):
    return model.trackID_to_trackName(catalog, track_id)

def albumID_to_albumType(catalog, albumID):
    return model.albumID_to_albumType(catalog, albumID)

def trackID_to_trackValue(catalog, trackID):
    return model.trackID_to_trackValue(catalog, trackID)

def albumID_to_albumName(catalog, albumID):
    return model.albumID_to_albumName(catalog, albumID)

def albumID_to_albumReleaseDate(catalog, albumID):
    return model.albumID_to_albumReleaseDate(catalog, albumID)

# ========================
# Funciones requerimientos
# ========================

def requerimiento1(catalog, year):
    return model.requerimiento1(catalog, year)

def requerimiento2(catalog, artist):
    return model.requerimiento2(catalog, artist)

def requerimiento3(catalog, track):
    return model.requerimiento3(catalog, track)

def requerimiento4(catalog, artista, mercado):
    return model.requerimiento4(catalog, artista, mercado)

def requerimiento5(catalogo, artista):
    return model.requerimiento5(catalogo, artista)

def requerimiento6(catalog, artista, mercado):
    return model.requerimiento6(catalog, artista, mercado)

# ========================================
# Funciones de pruebas de tiempo y memoria
# ========================================

    # =========================================
    # Funciones para medir tiempos de ejecucion
    # =========================================

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed




    # =========================================
    # Funciones para medir la memoria utilizada
    # =========================================

def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory