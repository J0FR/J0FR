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

from matplotlib import artist
from DISClib.ADT import list as lt
import config as cf
import model
import csv
import sys

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def newController(tipo_catalogo):

    control = {'model':None
    }

    control['model'] = model.newCatalog(tipo_catalogo)
    model.ordenamientoShell(control['model']["tracks"], model.cmpTracksIDs)
    model.ordenamientoShell(control['model']["albums"], model.cmpAlbumsIDs)
    model.ordenamientoShell(control['model']["artists"], model.cmpArtistsIDs)
    return control

# Funciones para la carga de datos

def loadData(tamanio_archivo ,control):

    album_size = loadAlbums(tamanio_archivo, control)
    artist_size = loadArtists(tamanio_archivo, control)
    track_size = loadTracks(tamanio_archivo, control)
    
    return album_size, artist_size, track_size


def loadAlbums(tamanio_archivo, control):

    albumsfile = cf.data_dir + f'spotify-albums-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for album in reader:
      model.addAlbum(control, album)
    return model.size(control["model"]['albums'])
    

def loadArtists(tamanio_archivo, control):

    albumsfile = cf.data_dir + f'spotify-artists-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for artist in reader:
      model.addArtists(control, artist)
    return model.size(control["model"]['artists'])


def loadTracks(tamanio_archivo, control):

    albumsfile = cf.data_dir + f'spotify-tracks-utf8-{tamanio_archivo}.csv'
    reader = csv.DictReader(open(albumsfile, encoding='utf8'))
    for track in reader:
      model.addTrack(control, track)
    return model.size(control["model"]['tracks'])


# Funciones para la creacion de datos

def getAlbumID(lst) -> list:
  return model.getAlbumID(lst)

def linearSearch_Requerimiento6(lst, AlbumIDList):
  return model.linearSearch_Requerimiento6(lst, AlbumIDList)#


def interpolationSearch_Requerimiento1(lst, pos1, lst_size, elementToFind, primeroUltimo):
  return model.interpolationSearch_Requerimiento1(lst, pos1, lst_size, elementToFind, primeroUltimo) #

def binarySearchLimites(lst, elemento, elementoDiccionario, primeroUltimo):
  return model.binarySearchLimites(lst, elemento, elementoDiccionario, primeroUltimo)

def binarySearchLimites_years(lst, elemento, elementoDiccionario, primeroUltimo):
  return model.binarySearchLimites_years(lst, elemento, elementoDiccionario, primeroUltimo)


def listaArtistasID(lst, datos):
  
  lista = model.ordenamientoMerge(lst,"artists", (model.cmpArtistsID_tracksID,))
  string = ""
  for i in datos:
    string += lt.getElement(lista, model.binarySearch(lista, i, "id"))["name"] + ", "
  return string#S

  
def binarySearch(lst, elemento, elementoDiccionario):
  return model.binarySearch(lst, elemento, elementoDiccionario)

# generalizarlo
def binarySearchLimites_tracks(control, elemento, primeroUltimo):
  return model.binarySearchLimites(control["model"]["tracks"], elemento, "artists_id", primeroUltimo)

def linearSearch_Requerimiento4(lst, element, mercado):
  return model.linearSearch_Requerimiento4(lst, element, mercado) #

def contador_elementos(lst, element):
  return model.contador_elementos(lst, element) #


# Funciones de comparacion
def cmpArtistsByFollowers(artist1, artist2):
  return model.cmpArtistsByFollowers(artist1, artist2)

def cmpTracksPopularity(track1, track2):
  return model.cmpTracksPopularity(track1, track2)



def buscarCancionPorID(control, elementoBuscado):
  lista_ordenada = model.ordenamientoShell(control["model"]["albums"], model.cmpIDTracks)
  index = model.binarySearch(lista_ordenada, elementoBuscado, "id")
  if index == -1:
    return "Not found"
  else:
    return lt.getElement(lista_ordenada, index)["name"]#

def albumName_Requerimiento4(control, elemento):
  lista = model.ordenamientoShell(control["model"]["albums"], model.cmpAlbumsIDs)
  return lt.getElement(lista ,binarySearch(lista, elemento, "id"))["name"] #

def listaArtistas_IDaNombre(control, lista_artistas):
  lista = model.ordenamientoShell(control["model"]["artists"] , model.cmpArtistsID_tracksID)
  string = ""
  for i in lista_artistas:
    string += lt.getElement(lista, binarySearch(lista, i, "id"))["name"] + ", "
  return string[:-2] #

def buscarIDArtista(control, elementoBuscado):
  lista_ordenada = model.ordenamientoShell(control["model"]["artists"] , model.cmpArtistsByName)
  index = model.binarySearch(lista_ordenada, elementoBuscado, "name")
  if index == -1:
    return "Not found"
  else:
    return lt.getElement(lista_ordenada, index)["id"] #














# Funcionalidades ADT Crudas

def isEmpty(lst):
    return model.isEmpty(lst)

def size(lst):
    return model.size(lst)

def getElement(lst, pos):
    return model.getElement(lst, pos)

def deleteElement(lst, pos):
    return model.deleteElement(lst, pos)

def subList(lst, pos, numelem):
    return model.subList(lst, pos, numelem)

def iterator(lst):
    return model.iterator(lst)



# Funciones de ordenamiento

def ordenamientoSelection(control, funcion):
  return model.ordenamientoSelection(control, funcion)

def ordenamientoInsetion(control, funcion):
  return model.ordenamientoInsetion(control, funcion)

def ordenamientoShell(lst, funcion):
  return model.ordenamientoShell(lst, funcion)

def ordenamientoMerge(control, funcion):
  return model.ordenamientoMerge(control, funcion)

def ordenamientoQuick(control, funcion):
  return model.ordenamientoQuick(control, funcion)


# Funciones de busqueda



# Funciones para sacar datos

def FirstThreeLastThree(list, list_size):
  firstThree, lastThree = model.firstThreeLastThree(list, list_size)
  return firstThree, lastThree #


# Funciones de comparacion

def cmpTracksIDs(FirstTrack, SecondTrack):
    return model.cmpTracksIDs(FirstTrack, SecondTrack)

def cmpAlbumsIDs(FirstAlbum, SecondAlbum):
    return model.cmpAlbumsIDs(FirstAlbum, SecondAlbum)

def cmpArtistsIDs(FirstArtist, SecondArtist):
    return model.cmpArtistsIDs(FirstArtist, SecondArtist)

# Funciones para consola
def clearConsole():
    return model.clearConsole()


# Funciones requerimientos

  # Funciones requerimiento 5
def contarTiposDeAlbumes(lst):
  single = 0
  compilation = 0
  album = 0
  for _ in model.iterator(lst):
    if _["album_type"] == "single":
      single += 1
    elif _["album_type"] == "compilation":
      compilation += 1
    elif _["album_type"] == "album":
      album += 1
  return single, compilation, album


# Funciones busqueda ids
def idArtista_NombreArtista(lst_artists, idArtista):
  for _ in lt.iterator(lst_artists):
    if _["id"] == idArtista:
      return _["name"]
  return -1

# Funciones busqueda de id a nombre
def idArtista_NombreArtista(lst_artists, idArtista):
  return model.idArtista_NombreArtista(lst_artists, idArtista)

def idAlbum_NombreAlbum(lst_albums, idAlbum):
  return model.idAlbum_NombreAlbum(lst_albums, idAlbum)

def idTrack_NombreTrack(lst_tracks, idTrack):
  return model.idTrack_NombreTrack(lst_tracks, idTrack)

def requerimiento3_listArtistsID_listNames(control, listArtistsID):
  nombres = []
  if len(listArtistsID) == 0:
    return "No hay artistas"
  else:
    for _ in listArtistsID:
      nombres.append(idAlbum_NombreAlbum(control["model"]["artists"], _))
    return nombres




#Requerimientos

def Requerimiento1(control, inicial, final):
  organized = ordenamientoMerge(control['model']['albums'], model.cmpYearsMenorMayor)
  index_anio_inicial = interpolationSearch_Requerimiento1(organized, 1, lt.size(organized), inicial, True)
  index_anio_final = interpolationSearch_Requerimiento1(organized, 1, lt.size(organized), final, False)
  sublista = lt.subList(organized, index_anio_inicial, (index_anio_final - index_anio_inicial))
  albumFirstThree, albumLastThree = FirstThreeLastThree(sublista, size(sublista))
  return albumFirstThree, albumLastThree

def Requerimiento2(control, n):
  organized = ordenamientoMerge(control["model"]["artists"], model.cmpArtistsPopularity)
  top_n = lt.subList(organized, 1, n)
  albumFirstThree, albumLastThree = FirstThreeLastThree(top_n, size(top_n))
  return top_n, albumFirstThree, albumLastThree


def Requerimiento3(control, top):
  ordenado = model.ordenamientoMerge(control["model"]["tracks"], model.cmpTracksPopularity)
  TopTracks = model.buscarTracksTOP(ordenado, top)
  trackFirstThree, trackLastThree = FirstThreeLastThree(TopTracks, top)
  return TopTracks, trackFirstThree, trackLastThree

def Requerimiento4(control, artista, mercado):
  idArtista = buscarIDArtista(control, artista)
  cantidadCancionesArtista, cancionesDeArtista = linearSearch_Requerimiento4(control["model"]["tracks"], idArtista, mercado)
  canciones_organizadas = ordenamientoMerge(cancionesDeArtista, model.cmpTrackPopularity_duration_name)
  cantidadAlbunesArtista = contador_elementos(control["model"]["albums"], idArtista)
  return cantidadCancionesArtista, canciones_organizadas, cantidadAlbunesArtista

def Requerimiento5(control, nombreArtista):

  idArtista = buscarIDArtista(control, nombreArtista)
  listaAlbunesOrganizado_Nombres = ordenamientoMerge(control["model"]["albums"], model.cmpArtistID_Albums)
  indexAlbumArtistas_Inicial = model.binarySearchLimites(listaAlbunesOrganizado_Nombres, idArtista, "artist_id", True)
  indexAlbumArtistas_Final = model.binarySearchLimites(listaAlbunesOrganizado_Nombres, idArtista, "artist_id", False)
  subLista_albums = lt.subList(listaAlbunesOrganizado_Nombres, indexAlbumArtistas_Inicial, (indexAlbumArtistas_Final - indexAlbumArtistas_Inicial)+1)
  single, compilation, album = contarTiposDeAlbumes(subLista_albums)
  albumFirstThree, albumLastThree = FirstThreeLastThree(subLista_albums, size(subLista_albums))
  return single, compilation, album, albumFirstThree, albumLastThree

def Requerimiento6(control, anio_inicial,anio_final):
  organizedAlbumsByYear = ordenamientoMerge(control['model']['albums'], model.cmpYearsMenorMayor)
  anio_inicial_index = interpolationSearch_Requerimiento1(organizedAlbumsByYear, 1, size(organizedAlbumsByYear), anio_inicial, True)
  anio_final_index = interpolationSearch_Requerimiento1(organizedAlbumsByYear, 1, size(organizedAlbumsByYear), anio_final, False)
  sublista = lt.subList(organizedAlbumsByYear, anio_inicial_index, anio_final_index-anio_inicial_index)
  getAlbumIDList = getAlbumID(sublista)
  canciones = linearSearch_Requerimiento6(control["model"]["tracks"], getAlbumIDList)
  organizarCanciones_available_markets = ordenamientoMerge(canciones, model.cmpAvailableMarkets_popularity_name)
  return organizarCanciones_available_markets
  