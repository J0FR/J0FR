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
import csv
import controller
import csv
from DISClib.ADT import list as lt
from prettytable import PrettyTable
assert cf
import model

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController(tipo_catalogo):

    control = controller.newController(tipo_catalogo)
    return control


def printMenu():
    controller.clearConsole()
    print("========== ¡Bienvenido! ==========\n")
    print("1- Cargar información en el catálogo")
    print("2- Listar los albumes en un periodo de tiempo")
    print("3- Encontrar los artistas mas populares")
    print("4- Encontrar las canciones mas populares")
    print("5- Encontrar la canción mas popular de un artista")
    print("6- Encontrar la discografia de un artista")
    print("7- Clasificar las canciones con mayor distribucion")
    print("0- Salir")


def loadData(tamanio_archivo):

    album, artist, track = controller.loadData(tamanio_archivo, control)
    return album, artist, track

# Prints
def print_artistFirstThreeLastThree(lista_primerosArtistas, lista_ultimosArtistas):
    x = PrettyTable()
    x.field_names = ['name', 'artist_popularity', 'followers', 'genres', "cancion_referente"]
    
    if lista_primerosArtistas:
        for _ in range(1,4):
            datos_artista = lt.getElement(lista_primerosArtistas, _)
            x.add_row([
                datos_artista['name'],
                datos_artista['artist_popularity'],
                datos_artista['followers'],
                ", ".join(datos_artista['genres']),
                controller.idTrack_NombreTrack(control["model"]["tracks"], datos_artista["track_id"]),
            ])

    if lista_ultimosArtistas:
        x.add_row(["...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "..."])
        for _ in range(1,4):
            datos_artista = lt.getElement(lista_ultimosArtistas, _)
            x.add_row([
                datos_artista['name'],
                datos_artista['artist_popularity'],
                datos_artista['followers'],
                ", ".join(datos_artista['genres']),
                controller.idTrack_NombreTrack(control["model"]["tracks"], datos_artista["track_id"]),
            ])
            
    print(x.get_string())

def print_albumFirstThreeLastThree(lista_primerosAlbums, lista_ultimosAlbums):
    x = PrettyTable()
    x.field_names = ['name', 'release_date', 'album_type', "artist", "total_tracks"]

    if lista_primerosAlbums:
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_primerosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['release_date'].year,
                datos_albums['album_type'],
                controller.idArtista_NombreArtista(control['model']["artists"],datos_albums["artist_id"]),
                datos_albums["total_tracks"]
            ])

    if lista_ultimosAlbums:
        x.add_row(["...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "..."])
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_ultimosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['release_date'].year,
                datos_albums['album_type'],
                controller.idArtista_NombreArtista(control['model']["artists"],datos_albums["artist_id"]),
                datos_albums["total_tracks"]
            ])

    print(x.get_string())


def print_trackFirstThreeLastThree(lista_primerosAlbums, lista_ultimosAlbums):
    x = PrettyTable()
    x.field_names = ['name', 'popularity', 'disc_number', 'track_number', 'duration_ms', 'href']

    if lista_primerosAlbums:
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_primerosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['popularity'],
                datos_albums['disc_number'],
                datos_albums['track_number'],
                datos_albums['duration_ms'],
                datos_albums['href'],
            ])

    if lista_ultimosAlbums:
        x.add_row(["...", "...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "...", "..."])
        for _ in range(1,4):
            datos_albums = lt.getElement(lista_ultimosAlbums, _)
            x.add_row([
                datos_albums['name'],
                datos_albums['popularity'],
                datos_albums['disc_number'],
                datos_albums['track_number'],
                datos_albums['duration_ms'],
                datos_albums['href'],
            ])

    print(x.get_string())

def print_requerimiento2(lista, n):
    x = PrettyTable()
    x.field_names = ['artist_popularity', 'followers', 'name', 'relevant_track_name', 'genres']
    for _ in range(1, n):
        datos = lt.getElement(lista, _)
        x.add_row([
            datos['artist_popularity'],
            datos['followers'],
            datos['name'],
            controller.buscarCancionPorID(control, datos['track_id']),
            ", ".join(datos['genres'])       
        ])
    print(x.get_string())

def print_requerimiento3(FirstThree, LastThree):
    x = PrettyTable()
    x.field_names = ['name', 'album', 'artists', 'popularity', 'duration_ms', 'href','lyrics']
    if LastThree:
        x.add_row(["...", "...", "...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "...", "...", "..."])
        for i in range(1, 4):

            datos_tracks = lt.getElement(LastThree, i)
            x.add_row([
                datos_tracks['name'],
                controller.idAlbum_NombreAlbum(control["model"]["albums"],datos_tracks['album_id']),
                ", ".join(controller.requerimiento3_listArtistsID_listNames(control, datos_tracks['artists_id'])),
                datos_tracks['popularity'],
                datos_tracks['duration_ms'],
                datos_tracks['href'][:15],
                datos_tracks['lyrics'][:15],

            ])
    print(x.get_string)
def print_Requerimiento4(lst):
    datos = lt.getElement(lst, 1)
    x = PrettyTable()
    x.field_names = ['name', 'album_name', "release_date", 'artists', 'duration_ms', 'popularity', 'preview_url', 'lyrics']
    lista_nombreArtistas = controller.listaArtistas_IDaNombre(control, datos['artists_id'])
    x.add_row([
        datos['name'],
        controller.idAlbum_NombreAlbum(control["model"]["albums"], datos['album_id']),
        datos["release_date"],
        lista_nombreArtistas,
        datos['duration_ms'],
        datos['popularity'],
        "Letra de la canción NO disponible" if datos['lyrics'] == "-99" else datos['lyrics']
            ])
    print(x.get_string())

def printCanciones_Requerimiento5(lst):
    for _ in lt.iterator(lst):
        x = PrettyTable()
        x.field_names = ['name', 'artists', 'duration_ms', 'popularity', 'preview_url', 'lyrics']
        print(f'Most popular track in "{lst["track_name"]}')
        x.add_row([
                _['name'],
                _['artist_id'],
                _['total_tracks'],
                _['album_type'],
                _['artist_id'],
            ])
    print(x.get_string())

def print_Requerimiento6(lst, n):
    x = PrettyTable()
    x.field_names = ['name', "album_name", 'artists', 'avaliable_markets', 'popularity', 'duration_ms']

    for dato in lt.iterator(lst):
        x.add_row([
            dato['name'],
            controller.idAlbum_NombreAlbum(control["model"]["albums"],dato["album_id"]),
            ", ".join(controller.requerimiento3_listArtistsID_listNames(control, dato['artists_id'])),
            dato['available_markets_size'],
            dato['popularity'],
            dato['duration_ms']
                ])
    print(x.get_string())

def printFirstThreeLastThree_requerimiento5(FirstThree, LastThree):
    x = PrettyTable()
    x.field_names = ['release_date', 'album_name', 'total_tracks', 'album_type', 'artist_name']

    if FirstThree:
        for _ in range(1,4):
            datos_albums = lt.getElement(FirstThree, _)
            x.add_row([
                datos_albums['release_date'],
                datos_albums['name'],
                datos_albums['total_tracks'],
                datos_albums['album_type'],
                datos_albums['artist_id'],
            ])

    if LastThree:
        x.add_row(["...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "..."])
        x.add_row(["...", "...", "...", "...", "..."])
        for _ in range(1,4):
            datos_albums = lt.getElement(LastThree, _)
            x.add_row([
                datos_albums['release_date'],
                datos_albums['name'],
                datos_albums['total_tracks'],
                datos_albums['album_type'],
                datos_albums['artist_id'],
            ])
    print(x.get_string())



control = newController("SINGLE_LINKED")
"""
Menu principal
"""
while True:
    printMenu()
    opcionMenu = input('\nSeleccione una opción para continuar: ')
    controller.clearConsole()

    if int(opcionMenu[0]) == 1:
        inicio = model.getTime()
        tipo_catalogo = input("\n - - Con que tipo de representacion de lista quieres cargar el catalogo - - \n\n 1 - ARRAY_LIST \n 2 - SINGLE_LINKED \n\nSeleccion: ")
        control = newController(tipo_catalogo)
        controller.clearConsole()
        tamanio_archivo_input = input("\n - - Con que tipo tamaño quieres cargar el archivo - -\n- 5 \n- 10 \n- 20 \n- 30 \n- 50 \n- 80 \n- small \n- large\n\nSeleccion: ")
        print("\n\nCargando información de los archivos.....")
        if tamanio_archivo_input.isnumeric() == True:
            tamanio_archivo_input = tamanio_archivo_input+"pct"
        else:
            tamanio_archivo_input = tamanio_archivo_input
        album_size, artist_size, track_size = loadData(tamanio_archivo_input)
        
        artistFirstThree, artistLastThree = controller.FirstThreeLastThree(control["model"]["artists"], artist_size)
        albumFirstThree, albumLastThree = controller.FirstThreeLastThree(control["model"]["albums"], album_size)
        trackFirstThree, trackLastThree = controller.FirstThreeLastThree(control["model"]["tracks"], track_size)

        controller.clearConsole()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print('artist id count: ' + str(artist_size))
        print('albums id count: ' + str(album_size))
        print('tracks id count: ' + str(track_size))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        print("\n\nThe first 3 and last 3 artists in the range are...")
        print_artistFirstThreeLastThree(artistFirstThree, artistLastThree)
        print("\n\nThe first 3 and last 3 albums in the range are...")
        print_albumFirstThreeLastThree(albumFirstThree, albumLastThree)
        print("\n\nThe first 3 and last 3 tracks in the range are...")
        print_trackFirstThreeLastThree(trackFirstThree, trackLastThree)
        end = model.getTime()
        print(float(end-inicio))


        input("\n>Hundir cualquier tecla para continuar...")
        controller.clearConsole()
       


    elif int(opcionMenu[0]) == 2: # requerimiento 1
        print("========== Requerimiento 1 - Listar los albumes en un periodo de tiempo ==========\n")
        FechaInicialPeriodo = int(input("Introducir fecha inicial del periodo: "))
        FechaFinalPeriodo = int(input("Introducir fecha final del periodo: "))
        inicio = model.getTime()
        albumFirstThree, albumLastThree = controller.Requerimiento1(control, FechaInicialPeriodo, FechaFinalPeriodo)
        print_albumFirstThreeLastThree(albumFirstThree, albumLastThree)
        end = model.getTime()
        print(end-inicio)
        input("\n>Hundir cualquier tecla para continuar...")
        controller.clearConsole()


    elif int(opcionMenu[0]) == 3: # requerimiento 2
        print("========== Requerimiento 2 - Encontrar los artistas mas populares ==========\n")
        n = int(input("Ingrese la cantidad de artistas que quiere en su top: "))
        inicio = model.getTime()
        top_n, albumFirstThree, albumLastThree = controller.Requerimiento2(control, n)
        print_requerimiento2(top_n, controller.size(top_n))
        print_artistFirstThreeLastThree(albumFirstThree, albumLastThree)
        end = model.getTime()

        print(end-inicio)

        input("\n>Hundir cualquier tecla para continuar...")
        controller.clearConsole()

    elif int(opcionMenu[0]) == 4: # requerimiento 3
        print("========== Requerimiento 3 - Encontrar las canciones mas populares ==========\n")
        top = int(input("Ingrese el numero de las canciones más famosa, que desea conocer:"))
        inicio = model.getTime()
        canciones, trackFirstThree, trackLastThree = controller.Requerimiento3(control, top)
        print_requerimiento3(trackFirstThree,trackLastThree)
        end = model.getTime()
        print(end-inicio)
        input("\n>Hundir cualquier tecla para continuar...")
        controller.clearConsole()

    elif int(opcionMenu[0]) == 5: # requerimiento 4
        print("========== Requerimiento 4 - Encontrar la cancion mas popular de un artista ==========\n")
        artista = input("Inserte el nombre del artista: ")
        mercado = input("Nombre de país/mercado disponible de la canción: ")
        inicio = model.getTime()
        cantidadCancionesArtista, canciones_organizadas, cantidadAlbunesArtista = controller.Requerimiento4(control, artista, mercado)
        print(f"El número total de canciones del artista {artista} es: {cantidadCancionesArtista}")
        print(f"El número de álbumes asociados a el artista {artista} es: {cantidadAlbunesArtista}")
        print_Requerimiento4(canciones_organizadas)
        end = model.getTime()
        print(end-inicio)
        input("\n>Hundir cualquier tecla para continuar...")
        controller.clearConsole()

    elif int(opcionMenu[0]) == 6: # requerimiento 5
        print("========== Requerimiento 5 - Encontrar la discografia de un artista ==========\n")
        nombreArtista = input("Nombre del artista: ")
        inicio = model.getTime()
        single, compilation, album, albumFirstThree, albumLastThree = controller.Requerimiento5(control, nombreArtista)
        print(f'Number of "single": {single}')
        print(f'Number of "compilation": {compilation}')
        print(f'Number of "album": {album}')
        # Requisito print primeros 3 y ultimos 3
        printFirstThreeLastThree_requerimiento5(albumFirstThree, albumLastThree)   
        end = model.getTime()
        print(end-inicio) 
        printFirstThreeLastThree_requerimiento5(albumFirstThree, albumLastThree)
        input("\n>Hundir cualquier tecla para continuar...")    

    elif int(opcionMenu[0]) == 7:
        anio_inicial = int(input("Año inicial del periodo: "))
        anio_final = int(input("Año final del periodo: "))
        n = int(input("El número (N) de canciones a identificar (ej.: TOP 3, 5, 10 o 20): "))
        inicio = model.getTime()
        organizarCanciones_available_markets = controller.Requerimiento6(control, anio_inicial, anio_final)
        organizedAlbumsByYear = controller.ordenamientoShell(control['model']['albums'], model.cmpYearsMenorMayor)
        
        anio_inicial_index = controller.binarySearchLimites_years(control["model"]["albums"], anio_inicial, "release_date", True)
        anio_final_index = controller.binarySearchLimites_years(control["model"]["albums"], anio_inicial, "release_date", False)
        sublista = lt.subList(organizedAlbumsByYear, anio_inicial_index, (anio_final_index-anio_inicial_index))

        getAlbumIDList = controller.getAlbumID(sublista)
        canciones = controller.linearSearch_Requerimiento6(control["model"]["tracks"], getAlbumIDList)

        organizarCanciones_available_markets = controller.ordenamientoShell(canciones, model.cmpAvailableMarkets_popularity_name)
        print("llegue aca")
        print_Requerimiento6(organizarCanciones_available_markets, n)
        end = model.getTime()
        print(end-inicio)
        input("\n>Hundir cualquier tecla para continuar...")
        controller.clearConsole()


    else:
        sys.exit(0)
sys.exit(0)
