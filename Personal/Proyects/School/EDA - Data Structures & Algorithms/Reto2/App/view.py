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

from matplotlib import artist
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys
import tracemalloc
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
from prettytable import PrettyTable
import pycountry
import pandas



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ====================================================
# Inicializacion de la comunicacion con el controlador
# ====================================================

def newCatalog():
    """
    Se crea una instancia del controlador
    """
    control = controller.newCatalog()
    return control




# ===================================
# Funciones para imprimir resultados
# ===================================

def printRequerimiento1(lst, cantidad_albumes, year):
    print("========= Req No. 1 Inputs =========")
    print(f"Albums released in {year}")
    print()
    print("========= Req No. 1 Answer =========")
    print(f"There are {cantidad_albumes} albums released in {year}")
    print()
    print(f"The first 3 and last 3 albums in {year} are...")
    table = PrettyTable()
    table.field_names = ["name", "release_date", "total_tracks", "album_type", "artist_album_name", "external_urls"]
    for _ in range(1, 4):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["name"], current_lst["release_date"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"][13:-2]])

    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])

    for _ in range(cantidad_albumes - 2, cantidad_albumes + 1):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["name"], current_lst["release_date"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"][13:-2]])
    return table.get_string()


def printRequerimiento2(lst, cantidad_artistas, popularity):
    print("========= Req No. 2 Inputs =========")
    print(f"The artists with popularity rating of: {popularity}")
    print()
    print("========= Req No. 2 Answer =========")
    print(f"There are {cantidad_artistas} artists with {popularity}")
    print()
    print(f"The first 3 and last 3 artists with {popularity} are...")
    table = PrettyTable()
    table.field_names = ["artist_popularity", "followers", "name", "relevant_track_name", "genres"]
    for _ in range(1, 4):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["artist_popularity"], current_lst["followers"], current_lst["name"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])

    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])

    for _ in range(cantidad_artistas - 2, cantidad_artistas + 1):
        current_lst = lt.getElement(lst, _)
        
        table.add_row([current_lst["artist_popularity"], current_lst["followers"], current_lst["name"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])
    return table.get_string()


def printRequerimiento3(lst, size, popularity):
    print("========= Req No. 3 Inputs =========")
    print(f"The trakcs with popularity rating of: {popularity}")
    print()
    print("========= Req No. 3 Answer =========")
    print(f"There are {size} tracks with {popularity}")
    print()
    print(f"The first 3 and last 3 tracks with {popularity} are...")
    table = PrettyTable()
    table.field_names= ['popularity','duration_ms','name_track', 'disc_number', 'track_number', 'album_name', 'artists_names', 'href', 'lyrics']
    for i in range(1, 4):
        current_lst = lt.getElement(lst, i)
        artists = ""
        for _ in current_lst["value"]["artists_id"]:
            artists += f"{controller.artistID_to_artistName(catalog, _)}, \n"
        table.add_row([current_lst['value']['popularity'], current_lst['value']['duration_ms'], current_lst['value']['name'], current_lst['value']['disc_number'],current_lst['value']['track_number'],controller.albumID_to_albumName(catalog, current_lst["value"]["album_id"]),artists,current_lst['value']['href'],current_lst['value']['lyrics'][0:10] if current_lst['value']['lyrics'] != "-99" else "Not found"])
   
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "..."])
   
    for _ in range(size - 2, size + 1):
        current_lst = lt.getElement(lst, _)
        artists = ""
        for _ in current_lst["value"]["artists_id"]:
            artists += f"{controller.artistID_to_artistName(catalog, _)}, \n"
        table.add_row([current_lst['value']['popularity'], current_lst['value']['duration_ms'], current_lst['value']['name'], current_lst['value']['disc_number'],current_lst['value']['track_number'],controller.albumID_to_albumName(catalog, current_lst["value"]["album_id"]),artists,current_lst['value']['href'],current_lst['value']['lyrics'][0:10] if current_lst['value']['lyrics'] != "-99" else "Not found"])
   
    return table.get_string()


def printRequerimiento4(lst, number_of_tracks, number_of_albums, artista, mercado):
    country_name = pycountry.countries.get(alpha_2=mercado)
    country_name = country_name.name
    print("========= Req No. 4 Inputs =========")
    print(f"'{artista}' Discrography metrics in {country_name} Code: {mercado}")
    print()
    print("========= Req No. 4 Answer =========")
    print(f"'{artista}' available discography in {country_name} ({mercado})")
    print(f"Unique available Albums: {number_of_albums}")
    print(f"Unique available Tracks: {number_of_tracks}")
    print()
    print(f"The first and last 3 tracks in the range are...")
    table = PrettyTable()
    table.field_names = ["popularity", "duration_ms", "name", "album_type", "available_markets"]
    for _ in range(1, 4):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["popularity"], current_lst["duration_ms"], current_lst["name"], controller.albumID_to_albumType(catalog, current_lst["album_id"]), ", ".join(current_lst['available_markets'])])

    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])

    for _ in range(number_of_tracks - 2, number_of_tracks + 1):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["popularity"], current_lst["duration_ms"], current_lst["name"], controller.albumID_to_albumType(catalog, current_lst["album_id"]), ", ".join(current_lst['available_markets'])])

    return table.get_string()

def printRequerimiento5(albums_artista, numberItems_AlbumsArtista, artista, compilations, singles, discography, firstAndLastThree_TrackId, firstAndLastThree_AlbumName):
    print("========= Req No. 5 Inputs =========")
    print(f"Discography metrics from {artista}")
    print()
    print("========= Req No. 5 Answer =========")
    print(f"Number of 'compilations': {compilations}")
    print(f"Number of 'singles': {singles}")
    print(f"Number of 'Discography': {discography}")
    print()
    print("+++ Albums Details +++")
    print("The first and last 3 tracks in the range are...")
    table = PrettyTable()
    table.field_names = ["release_date", "album_name", "total_tracks", "album_type", "artist_album_name", "external_urls"]
    for _ in range(1, 4):
        current_lst = lt.getElement(albums_artista, _)
        table.add_row([current_lst["release_date"], current_lst["name"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"]])

    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "..."])

    for _ in range(numberItems_AlbumsArtista - 2, numberItems_AlbumsArtista + 1):
        current_lst = lt.getElement(albums_artista, _)
        table.add_row([current_lst["release_date"], current_lst["name"], current_lst["total_tracks"], current_lst["album_type"], controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["external_urls"]])
    print(table.get_string())

    print()
    print()
    print("+++ Tracks Details +++")
    for _ in range(1, 7):
        currentTrack = controller.trackID_to_trackValue(catalog, lt.getElement(firstAndLastThree_TrackId, _))
        print(f"Most popular track in '{lt.getElement(firstAndLastThree_AlbumName, _)}'")
        table = PrettyTable()
        table.field_names = ["popularity", "duration_ms", "name_track", "track_number", "artists_names", "preview_url", "href"]
        if currentTrack == None: 
            table.add_row(["Not found", "Not found", "Not found", "Not found", "Not found", "Not found", "Not found"])
        else:
            artists = ""
            for _ in currentTrack["artists_id"]:
                artists += f"{controller.artistID_to_artistName(catalog, _)}, \n"
            table.add_row([currentTrack["popularity"], currentTrack["duration_ms"], currentTrack["name"], currentTrack["track_number"], artists, currentTrack["preview_url"], currentTrack["href"]])
        print(table.get_string())
    

def printCargaDatos(sizeAlbums, sizeArtists, sizeTracks, FirstThreeAlbums, LastThreeAlbums, FirstThreeArtists, LastThreeArtists, FirstThreeTracks, LastThreeTracks):
    print(" - - - - - - - - - - - - - - - - - - - - - - - ")
    print(f"artists ID count: {sizeArtists}")
    print(f"albums ID count: {sizeAlbums}")
    print(f"tracks ID count: {sizeTracks}")
    print(" - - - - - - - - - - - - - - - - - - - - - - - ")
    print()
    print("The first 3 and last 3 artists in the range are...")
    table = PrettyTable()
    table.field_names = ["name", "artist_popularity", "followers", "relevant_track_name", "genres"]
    for _ in range(1, 4):
        current_lst = lt.getElement(FirstThreeArtists, _)
        table.add_row([current_lst["name"], current_lst["artist_popularity"], current_lst["followers"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])

    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "..."])

    for _ in range(3 - 2, 3 + 1):
        current_lst = lt.getElement(LastThreeArtists, _)
        table.add_row([current_lst["name"], current_lst["artist_popularity"], current_lst["followers"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), ',\n'.join(current_lst["genres"])])
    print(table.get_string())

    print()
    print("The first 3 and last 3 albums in the range are...")
    table = PrettyTable()
    table.field_names = ["name", "release_date", "relevant_track_name", "artist_album_name", "total_tracks", "album_type", "external_urls"]
    for _ in range(1, 4):
        current_lst = lt.getElement(FirstThreeAlbums, _)
        table.add_row([current_lst["name"], current_lst["release_date"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["total_tracks"], current_lst["album_type"], current_lst["external_urls"][13:-2]])

    table.add_row(["...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "..."])

    for _ in range(3 - 2, 3 + 1):
        current_lst = lt.getElement(LastThreeAlbums, _)
        table.add_row([current_lst["name"], current_lst["release_date"], controller.trackID_to_trackName(catalog, current_lst["track_id"]), controller.artistID_to_artistName(catalog, current_lst["artist_id"]), current_lst["total_tracks"], current_lst["album_type"], current_lst["external_urls"][13:-2]])
    print(table.get_string())

    print()
    print("The first 3 and last 3 tracks in the range are...")
    table = PrettyTable()
    table.field_names = ["name", "popularity", "album_name", "disc_number", "track_number", "duration_ms", "artist_names", "href"]
    for _ in range(1, 4):
        current_lst = lt.getElement(FirstThreeTracks, _)
        artists = ""
        for _ in current_lst["artists_id"]:
            artists += f"{controller.artistID_to_artistName(catalog, _)}, \n"
        table.add_row([current_lst["name"], current_lst["popularity"], controller.albumID_to_albumName(catalog, current_lst["album_id"]), current_lst["disc_number"], current_lst["track_number"], current_lst["duration_ms"], artists, current_lst["href"]])

    table.add_row(["...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "..."])

    for _ in range(3 - 2, 3 + 1):
        current_lst = lt.getElement(LastThreeTracks, _)
        artists = ""
        for _ in current_lst["artists_id"]:
            artists += f"{controller.artistID_to_artistName(catalog, _)}, \n"
        table.add_row([current_lst["name"], current_lst["popularity"], controller.albumID_to_albumName(catalog, current_lst["album_id"]), current_lst["disc_number"], current_lst["track_number"], current_lst["duration_ms"], artists, current_lst["href"]])
    print(table.get_string())


def printRequerimiento6(lst, lst_size, top, artist, pais):
    country_name = pycountry.countries.get(alpha_2=pais)
    country_name = country_name.name
    print("========= Req No. 6 Inputs =========")
    print(f"Top {top} tracks of {artist} in {country_name} CODE: {pais}")
    print()
    print("========= Req No. 6 Answer =========")
    print(f"There are {lst_size} tracks released by {artist} in {country_name} CODE: {pais}")
    print(f"The TOP {top} most popular tracks of this artist in Spotify are:")
    if top <= lst_size:
        table = PrettyTable()
        table.field_names = ["name", "album_name", "album_realease_date", "artists", "number_of_countries", "popularity", "duration_ms", "lyrics"]
        for _ in range(1, top + 1):
            current_lst = lt.getElement(lst, _)
            artists = ""
            for _ in current_lst["artists_id"]:
                artists += f"{controller.artistID_to_artistName(catalog, _)}, \n"
            table.add_row([current_lst["name"], controller.albumID_to_albumName(catalog, current_lst["album_id"]), controller.albumID_to_albumReleaseDate(catalog, current_lst["album_id"]), artists, len(current_lst["available_markets"]), current_lst["popularity"], current_lst["duration_ms"], current_lst["lyrics"][0:10]])
        print(table.get_string())
    else:
        print("No hay canciones suficientes para hacer su top")
    
    print()
    print()
    print("Primeras y ultimas tres de la lista...")

    table = PrettyTable()
    table.field_names = ["name", "album_name", "album_realease_date", "artists", "number_of_countries", "popularity", "duration_ms", "lyrics"]
    for _ in range(1, 4):
        current_lst = lt.getElement(lst, _)
        table.add_row([current_lst["name"], controller.albumID_to_albumName(catalog, current_lst["album_id"]), controller.albumID_to_albumReleaseDate(catalog, current_lst["album_id"]), artists, len(current_lst["available_markets"]), current_lst["popularity"], current_lst["duration_ms"], current_lst["lyrics"][0:10]])

    table.add_row(["...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "..."])

    for _ in range(lst_size - 2, lst_size + 1):
        current_lst = lt.getElement(lst, _)
        
        table.add_row([current_lst["name"], controller.albumID_to_albumName(catalog, current_lst["album_id"]), controller.albumID_to_albumReleaseDate(catalog, current_lst["album_id"]), artists, len(current_lst["available_markets"]), current_lst["popularity"], current_lst["duration_ms"], current_lst["lyrics"][0:10]])
    return table.get_string()



# ================================
# Funcion para inicializar el menu
# ================================

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Examinar los albumes en un anio de interes | Requerimiento 1")
    print("3- Encontrar los artistas por popularidad | Requerimiento 2 (Individual)")
    print("4- Encontrar las canciones por popularidad | Requerimiento 3 (Individual)")
    print("5- Encontrar la cancion mas popular de un artista | Requerimiento 4")
    print("6- Encontrar la discografia de un artista | Requerimiento 5")
    print("7- Clasificar las canciones de artistas con mayor distribucion | Requerimiento 6 (Bono)")


catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n> ')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = newCatalog()
        delta_time, delta_memory, sizeAlbums, sizeArtists, sizeTracks, FirstThreeAlbums, LastThreeAlbums, FirstThreeArtists, LastThreeArtists, FirstThreeTracks, LastThreeTracks = controller.loadData(catalog)
        printCargaDatos(sizeAlbums, sizeArtists, sizeTracks, FirstThreeAlbums, LastThreeAlbums, FirstThreeArtists, LastThreeArtists, FirstThreeTracks, LastThreeTracks)
        print("El tiempo que se demoró la carga fue de: ",{delta_time})
        print("La cantidad de memoria usada fue de: ", {delta_memory})

        
    elif int(inputs[0]) == 2:
        year = int(input("Introduzca el anio que desea consultar: "))
        
        tracemalloc.start()
        start_memory = controller.getMemory()
        start_time = controller.getTime()

        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()

        albumsLST, cantidad_albumes = controller.requerimiento1(catalog, year)

        print(printRequerimiento1(albumsLST, cantidad_albumes, year))
        print("El tiempo que se demoró fue de: ",{delta_time})
        print("La memoria que se usó fue de:", {delta_memory})

    elif int(inputs[0]) == 3:
        popularity = int(input("Introduzca la popularidad que desea consultar: "))

        tracemalloc.start()
        start_memory = controller.getMemory()
        start_time = controller.getTime()

        artistLST, numero_canciones = controller.requerimiento2(catalog, popularity)

        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()

        delta_time = controller.deltaTime(stop_time, start_time)
        delta_memory = controller.deltaMemory(stop_memory, start_memory)

        print(printRequerimiento2(artistLST, numero_canciones, popularity))
        print("El tiempo que se demoró fue de: ",{delta_time})
        print("La memoria que se usó fue de:", {delta_memory})

    elif int(inputs[0]) == 4:
        popularity = int(input("Ingrese la popularidad que desea consultar (0-100):"))

        tracemalloc.start()
        start_memory = controller.getMemory()
        start_time = controller.getTime()

        tracks, lstsize = controller.requerimiento3(catalog, popularity)

        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()

        delta_time = controller.deltaTime(stop_time, start_time)
        delta_memory = controller.deltaMemory(stop_memory, start_memory)

        print(printRequerimiento3(tracks, lstsize, popularity))
        print("El tiempo que se demoró fue de: ",{delta_time})
        print("La memoria que se usó fue de:", {delta_memory})

        
    elif int(inputs[0]) == 5:
        artista = input("Introduzca el artista que desea consultar: ")
        mercado = input("Introduzca el mercado que desea consultar: ")

        tracemalloc.start()
        start_memory = controller.getMemory()
        start_time = controller.getTime()

        lst_canciones, number_of_tracks, number_of_albums = controller.requerimiento4(catalog, artista, mercado)
        
        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()

        delta_time = controller.deltaTime(stop_time, start_time)
        delta_memory = controller.deltaMemory(stop_memory, start_memory)
        #print(lt.firstElement(canciones))
        print(printRequerimiento4(lst_canciones, number_of_tracks, number_of_albums, artista, mercado))
        print("El tiempo que se demoró fue de: ",{delta_time})
        print("La memoria que se usó fue de:", {delta_memory})

    elif int(inputs[0]) == 6:
        artista = input("Introduzca el artista que desea consultar: ")

        tracemalloc.start()
        start_memory = controller.getMemory()
        start_time = controller.getTime()

        albums_artista, numberItems_AlbumsArtista, firstAndLastThree_TrackId, firstAndLastThree_AlbumName, album_sencillo, album_recopilacion, album_album = controller.requerimiento5(catalog, artista)
        
        stop_time = controller.getTime()
        stop_memory = controller.getMemory()
        tracemalloc.stop()

        delta_time = controller.deltaTime(stop_time, start_time)
        delta_memory = controller.deltaMemory(stop_memory, start_memory)
        #print(album_recopilacion)
        #print(album_sencillo)
        #print(album_album)
        # Falta debug sorting
        print(printRequerimiento5(albums_artista, numberItems_AlbumsArtista, artista, album_recopilacion, album_sencillo, album_album, firstAndLastThree_TrackId, firstAndLastThree_AlbumName))
        print("El tiempo que se demoró fue de: ",{delta_time})
        print("La memoria que se usó fue de:", {delta_memory})


    elif int(inputs[0]) == 7:
        artista = input("Introduzca el artista que desea consultar: ")
        mercado = input("Introduzca el mercado que desea consultar: ")
        top = int(input("Introduzca la cantidad de canciones que desea que esten en su top: "))
        canciones, number_of_tracks = controller.requerimiento6(catalog, artista, mercado)
        printRequerimiento6(canciones, number_of_tracks, top, artista, mercado)


    else:
        sys.exit(0)
sys.exit(0)

# Various Artists