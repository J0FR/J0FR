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


from platform import release
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort
import datetime
import time
assert cf
import csv
import sys
import os

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo_catalogo):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'tracks': None,
               'albums': None,
               'artists': None}

    tipo = None
    if tipo_catalogo.lower() == 'array_list':
        tipo = 'ARRAY_LIST'
    elif tipo_catalogo.lower() == 'single_linked':
        tipo = 'SINGLE_LINKED'

    catalog['tracks'] = lt.newList(tipo, cmpTracksIDs)
    catalog['albums'] = lt.newList(tipo, cmpAlbumsIDs)
    catalog['artists'] = lt.newList(tipo, cmpArtistsIDs)

    return catalog

# Funciones para agregar informacion al catalogo

def addTrack(control, track):
    # Se adiciona el track a la lista de tracks
    t = newTrack(
        track['id'],
        track['href'],
        track['album_id'],
        track['key'],
        track['track_number'],
        track['artists_id'],
        track['energy'],
        track['loudness'],
        track['valence'],
        track['danceability'],
        track['playlist'],
        track['speechiness'],
        track['popularity'],
        track['liveness'],
        track['tempo'],
        track['duration_ms'],
        track['acousticness'],
        track['available_markets'],
        track['lyrics'],
        track['disc_number'],
        track['instrumentalness'],
        track['preview_url'],
        track['name']
        )
    lt.addLast(control['model']['tracks'], t)
    return control


def addAlbum(control, albums):
    # Se adiciona el album a la lista de albums
    t = newAlbum(
        albums['id'],
        albums['track_id'],
        albums['total_tracks'],
        albums['external_urls'],
        albums['album_type'],
        albums['available_markets'],
        albums['artist_id'],
        albums['images'],
        albums['release_date'],
        albums['name'],
        albums['release_date_precision']
        )
    lt.addLast(control['model']['albums'], t)
    return control


def addArtists(control, artist):
    # Se adiciona el album a la lista de albums
    t = newArtist(
        artist['id'],
        artist['track_id'],
        artist['artist_popularity'],
        artist['genres'],
        artist['name'],
        artist['followers']
        )
    lt.addLast(control['model']['artists'], t)

# Funciones para creacion de datos

def newAlbum(
    id,
    track_id,
    total_tracks,
    external_urls,
    album_type,
    available_markets,
    artist_id,
    images,
    release_date,
    name,
    release_date_precision
    ):

    album = {
        'id': '',
        'track_id': '',
        'total_tracks': '',
        'external_urls': '',
        'album_type': '',
        'available_markets': '',
        'artist_id': '',
        'images': '',
        'release_date': '',
        'name': '',
        'release_date_precision': ''
            }

    album['id'] = id
    album['track_id'] = track_id
    album['total_tracks'] = float(total_tracks)
    album['external_urls'] = external_urls
    album['album_type'] = album_type
    album['available_markets'] = (available_markets.replace("[", "").replace("]", "").replace("'", "").replace('"', "")).split(",")
    album['artist_id'] = artist_id
    album['images'] = images
    album['release_date'] = datetime.datetime.strptime(release_date, "%Y-%m-%d") if (len(release_date) == 10) else (datetime.datetime.strptime(release_date[:4] + "19" + release_date[-2:], "%b-%Y") if (len(release_date) == 6) else (datetime.datetime.strptime(release_date, '%Y')))
    album['name'] = name
    album['release_date_precision'] = release_date_precision

    return album


def newTrack(
    id,
    href,
    album_id,
    key,
    track_number,
    artists_id,
    energy,
    loudness,
    valence,
    danceability,
    playlist,
    speechiness,
    popularity,
    liveness,
    tempo,
    duration_ms,
    acousticness,
    available_markets,
    lyrics,
    disc_number,
    instrumentalness,
    preview_url,
    name
    ):

    track = {
        'id': '',
        'href': '',
        'album_id': '',
        'key': '',
        'track_number': '',
        'artists_id': '',
        'energy': '',
        'loudness': '',
        'valence': '',
        'danceability': '',
        'playlist': '',
        'speechiness': '',
        'popularity': '',
        'liveness': '',
        'tempo': '',
        'duration_ms': '',
        'acousticness': '',
        'available_markets': '',
        'available_markets_size': '',
        'lyrics': '',
        'disc_number': '',
        'instrumentalness': '',
        'preview_url': '',
        'name': ''
            }

    available_markets = (available_markets.replace("[", "").replace("]", "").replace("'", "").replace('"', "")).split(",")
    track['id'] = id
    track['href'] = href
    track['album_id'] = album_id
    track['key'] = key
    track['track_number'] = track_number
    track['artists_id'] = (artists_id.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")).split(",")
    track['energy'] = energy
    track['loudness'] = loudness
    track['valence'] = valence
    track['danceability'] = danceability
    track['playlist'] = playlist
    track['speechiness'] = speechiness
    track['popularity'] = float(popularity)
    track['liveness'] = float(liveness)
    track['tempo'] = float(tempo)
    track['duration_ms'] = float(duration_ms)
    track['acousticness'] = acousticness
    track['available_markets'] = available_markets
    track['available_markets_size'] = len(available_markets)
    track['lyrics'] = lyrics
    track['disc_number'] = float(disc_number)
    track['instrumentalness'] = instrumentalness
    track['preview_url'] = preview_url
    track['name'] = name

    return track


def newArtist(
    id,
    track_id,
    artist_popularity,
    genres,
    name,
    followers
    ):

    artist = {
        'id': '',
        'track_id': '',
        'artist_popularity': '',
        'genres': '',
        'name': '',
        'followers': ''
            }

    artist['id'] = id
    artist['track_id'] = track_id
    artist['artist_popularity'] = float(artist_popularity)
    artist['genres'] = (genres.replace("[", "").replace("]", "").replace("'", "")).split(",")
    artist['name'] = name
    artist['followers'] = float(followers)

    return artist

# Funciones de consulta

def listSize(list):
    return lt.size(list)




def buscarTracksTOP(lst, top):
    TOPtracks = lt.subList(lst, 1, top)
    return TOPtracks #

def interpolationSearch_Requerimiento1(lst, pos1, lst_size, elementToFind, primeroUltimo):
    elementToFind = int(elementToFind)
 
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (pos1 <= lst_size and elementToFind >= lt.getElement(lst, pos1)["release_date"].year and elementToFind <= lt.getElement(lst, lst_size)["release_date"].year):
 
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = pos1 + ((lst_size - pos1) // (lt.getElement(lst, lst_size)["release_date"].year - lt.getElement(lst, pos1)["release_date"].year) * (elementToFind - lt.getElement(lst, pos1)["release_date"].year))
 
        # Condition of target found
        if lt.getElement(lst, pos)["release_date"].year == elementToFind:
            if primeroUltimo == True:
                while lt.getElement(lst, pos-1)["release_date"].year == elementToFind:
                    pos -= 1
            else:
                while lt.getElement(lst, pos)["release_date"].year == elementToFind:
                    pos += 1
            return pos
 
        # If x is larger, x is in right subarray
        if lt.getElement(lst, pos)["release_date"].year < elementToFind:
            return interpolationSearch_Requerimiento1(lst, pos + 1, lst_size, elementToFind, primeroUltimo)
 
        # If x is smaller, x is in left subarray
        if lt.getElement(lst, pos)["release_date"].year > elementToFind:
            return interpolationSearch_Requerimiento1(lst, pos1, pos - 1, elementToFind, primeroUltimo)
    
    return -1 #

def binarySearch(lst, elemento, elementoDiccionario):
    low = 1
    high = lt.size(lst)
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if lt.getElement(lst, mid)[f"{elementoDiccionario}"] < elemento:
            low = mid + 1
        # If x is smaller, ignore right half
        elif lt.getElement(lst, mid)[f"{elementoDiccionario}"] > elemento:
            high = mid - 1
        # means x is present at mid
        else:
            return mid #
 
    # If we reach here, then the element was not present
    return -1


def binarySearchLimites(lst, elemento, elementoDiccionario, primeroUltimo):
    low = 1
    high = lt.size(lst)
    mid = 0
    while low <= high:
 
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if lt.getElement(lst, mid)[f"{elementoDiccionario}"] < elemento:
            low = mid + 1 
        # If x is smaller, ignore right half
        elif lt.getElement(lst, mid)[f"{elementoDiccionario}"] > elemento:
            high = mid - 1
        # means x is present at mid
        else:
            if primeroUltimo == True:
                while lt.getElement(lst, mid-1)[f"{elementoDiccionario}"] == elemento:
                    mid -= 1
                return mid
            else:
                while lt.getElement(lst, mid)[f"{elementoDiccionario}"] == elemento:
                    mid += 1
                return mid -1
 
    # If we reach here, then the element was not present
    return -1 #

def binarySearchLimites_years(lst, elemento, elementoDiccionario, primeroUltimo):
    low = 1
    high = lt.size(lst)
    mid = 0
    while low <= high:
 
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if lt.getElement(lst, mid)[f"{elementoDiccionario}"].year < elemento:
            low = mid + 1 
        # If x is smaller, ignore right half
        elif lt.getElement(lst, mid)[f"{elementoDiccionario}"].year > elemento:
            high = mid - 1
        # means x is present at mid
        else:
            if primeroUltimo == True:
                while lt.getElement(lst, mid-1)[f"{elementoDiccionario}"].year == elemento:
                    mid -= 1
                return mid
            else:
                while lt.getElement(lst, mid)[f"{elementoDiccionario}"].year == elemento:
                    mid += 1
                return mid -1
 
    # If we reach here, then the element was not present
    return -1 #

def getAlbumID(lst) -> list:
    AlbumIDList = []
    for i in lt.iterator(lst):
        AlbumIDList.append(i["id"])

    return AlbumIDList


def linearSearch_Requerimiento4(lst, element, mercado):
    subLista = lt.newList("ARRAY_LIST")
    contador = 0
    for i in range(1, lt.size(lst)):
        if (element in lt.getElement(lst, i)["artists_id"]):
            contador += 1
        if (element in lt.getElement(lst, i)["artists_id"]) and (mercado in lt.getElement(lst, i)['available_markets']):
            lt.addLast(subLista, lt.getElement(lst, i))
  
    return contador, subLista


def linearSearch_Requerimiento6(lst, AlbumIDList):
    subLista = lt.newList("ARRAY_LIST")
    for i in lt.iterator(lst):
        if (i["album_id"] in AlbumIDList):
            lt.addLast(subLista, i)
            
    return subLista #

def contador_elementos(lst, element):
    contador = 0 
    for i in range(1, lt.size(lst)):
        if element == lt.getElement(lst, i)["artist_id"]:
            contador += 1
    return contador






# Funciones de comparacion

def cmpArtistsByFollowers(artist1, artist2): 
    """ Devuelve verdadero (True) si los 'followers' de artist1 son menores que los del artist2 Args: artist1: informacion del primer artista que incluye su valor 'followers' artist2: informacion del segundo artista que incluye su valor 'followers' """
    return artist1["followers"] < artist2["followers"]

def cmpYearsMenorMayor(date1, date2):
    return (date1["release_date"].year < date2["release_date"].year)#

def cmpYearsMayorMenor(date1, date2):
    return (date1["release_date"].year > date2["release_date"].year)

def cmpArtistsPopularity(artist1, artists2):
    if artist1["artist_popularity"] != artists2["artist_popularity"]:
        return artist1["artist_popularity"] > artists2["artist_popularity"]
    elif artist1["followers"] != artists2["followers"]:
        return artist1["followers"] > artists2["followers"]
    else:
        return artist1["name"] > artists2["name"]#

def cmpIDTracks(artist1, artist2):
    return artist1["id"] < artist2["id"]

def cmpArtistsID(artist1, artist2):
    return artist1["artists_id"] < artist2["artists_id"]

def cmpArtistsID_tracksID(artist1, artist2):
    return artist1["id"] < artist2["id"] #

def cmpArtistID_Albums(album1, album2):
    return album1["artist_id"] < album2["artist_id"]


def cmpTrackPopularity_duration_name(track1, track2):
    if track1["popularity"] != track2["popularity"]:
            return track1["popularity"] > track2["popularity"]
    elif track1["duration_ms"] != track2["duration_ms"]:
        return track1["duration_ms"] > track2["duration_ms"]
    else:
        return track1["name"] > track2["name"]#
    
def cmpAvailableMarkets_popularity_name(track1, track2):
    if track1["available_markets_size"] != track2["available_markets_size"]:
            return track1["available_markets_size"] > track2["available_markets_size"]
    elif track1["popularity"] != track2["popularity"]:
        return track1["popularity"] > track2["popularity"]
    else:
        return track1["name"] > track2["name"]#

def cmpTracksPopularity(track1, track2):
    if track1["popularity"] != track2["popularity"]:
            return track1["popularity"] > track2["popularity"]
    elif track1["duration_ms"] != track2["duration_ms"]:
        return track1["duration_ms"] > track2["duration_ms"]
    else:
        return track1["name"] > track2["name"]

def cmpArtistsByName(artist1, artist2):
    return artist1["name"] < artist2["name"] #








# Funcionalidades ADT Crudas

def isEmpty(lst):
    return lt.isEmpty(lst)

def size(lst):
    return lt.size(lst)

def getElement(lst, pos):
    return lt.getElement(lst, pos)

def deleteElement(lst, pos):
    return lt.deleteElement(lst, pos)

def subList(lst, pos, numelem):
    return lt.subList(lst, pos, numelem)

def iterator(lst):
    return lt.iterator(lst)



# Funciones de ordenamiento ADT

def ordenamientoSelection(lst, cmpfunction):
    return selectionsort.sort(lst, cmpfunction)
    
def ordenamientoInsetion(lst, cmpfunction):
    return insertionsort.sort(lst, cmpfunction)

def ordenamientoShell(lst, cmpfunction):
    return shellsort.sort(lst, cmpfunction)

def ordenamientoMerge(lst, cmpfunction):
    return mergesort.sort(lst, cmpfunction)

def ordenamientoQuick(lst, cmpfunction):
    return quicksort.sort(lst, cmpfunction)


# Funciones de busqueda

def buscarLimiteDeElemento(lst, element, limit, Dict_Key):
    # limite == True -> busca el limite superior, else -> limite inferior
    if limit == True:
        while lt.getElement(lst, mid-1)[f"{Dict_Key}"] == element:
            mid -= 1
    else:
        while lt.getElement(lst, mid)[f"{Dict_Key}"] == element:
            mid += 1
    return mid

def busquedaLineal(lst, lookingForElement, Dict_Key):
    for _ in range(1, lt.size(lst)):
        if _[f"{Dict_Key}"] == lookingForElement:
            return _
    return -1



# Funciones para sacar datos

def firstThreeLastThree(list, list_size):
    firstThree = lt.subList(list, 1, 3)
    lastThree = lt.subList(list, list_size-2, 3)
    return firstThree, lastThree



# Funciones para medir tiempos de ejecucion

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed



# Funciones de comparacion


# Funciones de comparacion de ordenamiento (Sorts)
    
def cmpTracksIDs(FirstTrack, SecondTrack):
    return FirstTrack["id"] < SecondTrack["id"]

def cmpAlbumsIDs(FirstAlbum, SecondAlbum):
    return FirstAlbum["id"] < SecondAlbum["id"] #

def cmpArtistsIDs(FirstArtist, SecondArtist):
    return FirstArtist["id"] < SecondArtist["id"]

# Funciones para consola
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Funciones busqueda de id a nombre
def idArtista_NombreArtista(lst_artists, idArtista):
    for _ in lt.iterator(lst_artists):
        if _["id"] == idArtista:
            return _["name"]
    return -1

def idAlbum_NombreAlbum(lst_albums, idAlbum):
    for _ in lt.iterator(lst_albums):
        if _["id"] == idAlbum:
            return _["name"]
    return -1

def idTrack_NombreTrack(lst_tracks, idTrack):
    for _ in lt.iterator(lst_tracks):
        if _["id"] == idTrack:
            return _["name"]
    return -1


def NombreTrack_IDTrack(lst_tracks, NombreTrack):
    index = binarySearch(lst_tracks, NombreTrack, "id")
    if index == -1:
        return "No disponible"
    return lt.getElement(lst_tracks, index)["name"]