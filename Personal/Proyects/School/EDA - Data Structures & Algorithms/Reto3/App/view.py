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
assert cf
from DISClib.ADT import list as lt
from prettytable import PrettyTable
from DISClib.ADT import map as mp
import time
from DISClib.DataStructures import mapentry as me




"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Reportar las cinco adquisiciones mas recientes e un club | Requerimiento #1 (Grupal)")
    print("2- Reportar los jugadores de cierta posicion detro de un rango de desempeño, potencial y salario | Requerimiento #2 (Grupal)")
    print("3- Reportar los jugadores dentro de un rango salarial y con cierta etiqueta | Requerimiento #3 (Individual)")
    print("4- Reportar los jugadores con cierto rasgo caracteristico y nacidos en un periodo de tiempo | Requerimiento #4 (Individual)")
    print("5- Graficar el historigrama de una propiedad para los jugadores de FIFA | Requerimiento #5 (Grupal)")
    print("6- Encontrar posibles sustituciones para los jugadores FIFA | Requerimiento #6 (Bono)")
    print("7- Cargar información en el catálogo")
    print("8- Cualquier tecla para salir")


def AskForFileSize():
    controller.clearConsole()
    print("Cual archivo te gustaria cargar?")
    print("1- Small\n" +
          "2- Large\n" +
          "3- 5%\n" +
          "4- 10%\n" +
          "5- 20%\n" +
          "6- 30%\n" +
          "7- 50%\n" +
          "8- 80%\n")
    try:
        size = int(input("> "))
        if (size < 1) or (size > 8):
            controller.clearConsole()
            print("Por favor introduzca una opcion valida")
            input("\n> Hundir cualquier tecla para continuar...")
            size = AskForFileSize()
    except:
        controller.clearConsole()
        print("Por favor introduzca una opcion valida")
        input("\n> Hundir cualquier tecla para continuar...")
        size = AskForFileSize()
    controller.clearConsole()
    return size


def getFileSize():
    file = "fifa-players-2022-utf8-"
    fileSize = AskForFileSize()
    if fileSize == 1:
        file += "small.csv"
    elif fileSize == 2:
        file += "large.csv"
    elif fileSize == 3:
        file += "5pct.csv"
    elif fileSize == 4:
        file += "10pct.csv"
    elif fileSize == 5:
        file += "20pct.csv"
    elif fileSize == 6:
        file += "30pct.csv"
    elif fileSize == 7:
        file += "50pct.csv"
    elif fileSize == 8:
        file += "80pct.csv"
    return file        


def printPrimerosCinco_UltimosCinco_Players(lstPlayers, lstSize):
    table = PrettyTable()
    table.field_names = ["Nombre", "Edad", "Altura", "Peso", "Nacionalidad", "Valor (€)", "Salario (€)", "Clausula de liberacion (€)", "Liga", "Club", "Fecha de vinculacion", "Posiciones", "Reputacion", "Tags", "Comentarios"]
    table.max_table_width = 120
    table.max_width = 20
    for _ in range(1, 6):
        player = controller.lstGet(lstPlayers, _)
        player = controller.lstGet(player, 1)
        table.add_row([player["short_name"],
                       player["age"],
                       player["height_cm"],
                       player["weight_kg"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["release_clause_eur"],
                       player["league_name"],
                       player["club_name"],
                       player["club_joined"],
                       player["player_positions"],
                       player["international_reputation"],
                       player["player_tags"],
                       player["player_traits"],
                       ])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    for _ in range(lstSize - 4, lstSize + 1):
        player = controller.lstGet(lstPlayers, _)
        player = controller.lstGet(player, 1)
        table.add_row([player["short_name"],
                       player["age"],
                       player["height_cm"],
                       player["weight_kg"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["release_clause_eur"],
                       player["league_name"],
                       player["club_name"],
                       player["club_joined"],
                       player["player_positions"],
                       player["international_reputation"],
                       player["player_tags"],
                       player["player_traits"],
                       ])
    return print(table.get_string())


def printRequerimiento1(club, matrixDeJugadores, numeroAdquisiciones, ligaALaQuePertenece, tamanioMatrix, league_level):
    print("================== Req No. 1 Inputs ==================")
    print(f"The top 5 most recent adquisitions of the '{club}'")
    print()
    print("================== Req No. 1 Answer ==================")
    print(f"The '{club} has {numeroAdquisiciones} adquisitons'")
    print()
    print("- - - - - - - League Details - - - - - - -")
    print(f"     * Name: '{ligaALaQuePertenece}'")
    print(f"     * Category: '{league_level}'")
    print()
    print("The last 3 adquisitions are:")
    contador = 0
    table = PrettyTable()
    table.field_names = ["Nombre", "Edad", "Fecha de nacimiento", "Nacionalidad", "Valor Contrato", "Salario Jugador", "Valor Clausula Liberacion", "Fecha Vinculaicon a club", "Posiciones", "Comentarios", "Tags"]
    table.max_table_width = 120
    table.max_width = 20
    for _ in range(1, tamanioMatrix + 1):
        if contador == 5:
            break
        prePlayer = controller.lstGet(matrixDeJugadores, _)
        player = controller.lstGet(prePlayer, 1)
        table.add_row([player["short_name"],
                    player["age"],
                    player["dob"],
                    player["nationality_name"],
                    player["value_eur"],
                    player["wage_eur"],
                    player["release_clause_eur"],
                    player["club_joined"],
                    player["player_positions"],
                    player["player_traits"],
                    player["player_tags"],
                    ])
        contador += 1
    return print(table.get_string())


def printRequerimiento2(lstPlayers, lstSize, playerPosition, totalPlayerAmmount, limInferiorDesempenio, limSuperiorDesempenio, limInferiorPotencial, limSuperiorPotencial, limInferiorSalario, limSuperiorSalario):
    print("================== Req No. 2 Inputs ==================")
    print(f"Search for players in position '{playerPosition}'")
    print("- - - - With search Ranges of - - - -")
    print(f"     * 'overall' range between '{limInferiorDesempenio}' and '{limSuperiorDesempenio}'")
    print(f"     * 'potential' range between '{limInferiorPotencial}' and '{limSuperiorPotencial}'")
    print(f"     * 'wage_eur' range between '{limInferiorSalario}' and '{limSuperiorSalario}'")
    print()
    print("================== Req No. 2 Answer ==================")
    print(f"Available FIFA players: {totalPlayerAmmount}")
    print(f"Players found in range: {lstSize} and position: {playerPosition}")
    print("The first 3 and last 3 players in range are:")
    table = PrettyTable()
    table.field_names = ["Nombre", "Edad", "Fecha de nacimiento", "Nacioinalidad", "Valor de contrato", "Salario", "Valor clausula de liberacion", "Potencial", "Desempenio", "Posiciones del jugador", "Comentarios", "Etiquetas"]
    if lstSize < 6:
        print("No hay suficiente cantidad de elementos para imprimir la tabla correctamente (minimo 6 para dar los 3 primero y ultimos)")
        for _ in lt.iterator(lstPlayers):
            player = controller.lstGet(_, 1)
            table.add_row([player["short_name"],
                        player["age"],
                        player["dob"],
                        player["nationality_name"],
                        player["value_eur"],
                        player["wage_eur"],
                        player["release_clause_eur"],
                        player["potential"],
                        player["overall"],
                        player["player_positions"],
                        player["player_traits"],
                        player["player_tags"]
                        ])
        return print(table.get_string())
    for _ in range(1, 4):
        player = controller.lstGet(lstPlayers, _)
        player = controller.lstGet(player, 1)
        table.add_row([player["short_name"],
                       player["age"],
                       player["dob"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["release_clause_eur"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["player_traits"],
                       player["player_tags"]
                       ])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    for _ in range(lstSize - 2, lstSize + 1):
        player = controller.lstGet(lstPlayers, _)
        player = controller.lstGet(player, 1)
        table.add_row([player["short_name"],
                       player["age"],
                       player["dob"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["release_clause_eur"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["player_traits"],
                       player["player_tags"]
                       ])
    return print(table.get_string())


def printRequerimiento3(lstPlayers, lstSize, tag, limInf, limSup, playerAmmount):
    print("================== Req No. 3 Inputs ==================")
    print(f"Search for players with tag: '{tag}'")
    print("- - - - With search ranges of - - - -")
    print(f"     * 'wage_eur' range between '{limInf}' and '{limSup}'")
    print()
    print("================== Req No. 3 Answer ==================")
    print(f"Available FIFA players: {playerAmmount}")
    print(f"Players found in range: {lstSize} and Tag: '{tag}'")
    print("The resutls are:")
    table = PrettyTable()
    table.field_names = ["Nombre", "Edad", "Fecha de nacimiento", "Nacioinalidad", "Valor de contrato", "Salario", "club", "Liga", "Potencial", "Desempenio", "Posiciones del jugador", "Comentarios", "Etiquetas"]
    table.max_table_width = 120
    table.max_width = 20
    if lstSize < 6:
        print("No hay suficiente cantidad de elementos para imprimir la tabla correctamente (minimo 6 para dar los 3 primero y ultimos)")
        for _ in lt.iterator(lstPlayers):
            player = controller.lstGet(_, 1)
            table.add_row([player["long_name"],
                       player["age"],
                       player["dob"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["club_name"],
                       player["league_name"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["player_traits"],
                       player["player_tags"]
                       ])
        return print(table.get_string())
    for _ in range(1, 4):
        player = controller.lstGet(lstPlayers, _)
        player = controller.lstGet(player, 0)
        table.add_row([player["long_name"],
                       player["age"],
                       player["dob"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["club_name"],
                       player["league_name"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["player_traits"],
                       player["player_tags"]
                       ])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    for _ in range(lstSize - 2, lstSize + 1):
        player = controller.lstGet(lstPlayers, _)
        player = controller.lstGet(player, 1)
        table.add_row([player["long_name"],
                       player["age"],
                       player["dob"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["club_name"],
                       player["league_name"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["player_traits"],
                       player["player_tags"]
                       ])
    return print(table.get_string())

def printRequerimiento4(players, size):
    table = PrettyTable()
    table.field_names = ["Dob", "Nombre Completo", "Edad", "Nacionalidad", "Valor de contrato", "Salario", "Club", "Liga", "Potencial", "Desempenio", "Posiciones del jugador", "Comentarios", "Etiquetas"]
    table.max_width = 15
    table.max_table_width = 100
    for i in range(1, 4):
        player = controller.lstGet(players, i)
        player = controller.lstGet(player, 0)
        table.add_row([player["dob"],
                       player["long_name"],
                       player["age"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["club_name"],
                       player["league_name"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["player_traits"],
                       player["player_tags"]
                       ])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
    for i in range(size - 2, size + 1):
        player = controller.lstGet(players, i)
        player = controller.lstGet(player, 0)
        table.add_row([player["dob"],
                       player["long_name"],
                       player["age"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["club_name"],
                       player["league_name"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["player_traits"],
                       player["player_tags"]
                       ])
    return print(table.get_string())


def printRequerimiento5(propiedad, segmentos, niveles, lstSizeJugadores, sizeMapa, razonDeCambio, lstConteo, lstMark, minKey, maxKey):
    print("=========== Req No. 5 Inputs ===========")
    print(f"Count map (histogram) of: '{propiedad}'")
    print(f"Number of bins: {segmentos}")
    print(f"Player scale: {niveles}")
    print()
    print(f"There are {lstSizeJugadores} player on record.")
    print(f"The histogram counts {sizeMapa} players.")
    print(f"{propiedad} Histogram with {segmentos} bins and '{niveles}' players per lvl mark.")
    table = PrettyTable()
    table.field_names = ["bin", "count", "lvl", "mark"]
    table.max_table_width = 120
    table.max_width = 20
    for _ in range(segmentos):
        elementos = controller.lstGet(lstConteo, _ + 1)
        marks = controller.lstGet(lstMark, _ + 1)
        marks_string = "*" * marks
        if _ == 0:
            minKey_act = minKey
            maxKey_act = minKey_act + razonDeCambio
            table.add_row([f"({round(minKey_act, 3)}, {round(maxKey_act, 3)}]",
                           elementos,
                           marks,
                           marks_string
                        ])
        elif _ == 6:
            minKey_act = maxKey_act
            maxKey_act = maxKey
            table.add_row([f"({round(minKey_act, 3)}, {round(maxKey_act, 3)}]",
                           elementos,
                           marks,
                           marks_string
                        ])
        else:
            minKey_act = maxKey_act
            maxKey_act = minKey_act + razonDeCambio
            table.add_row([f"({round(minKey_act, 3)}, {round(maxKey_act, 3)}]",
                           elementos,
                           marks,
                           marks_string
                        ])
    return print(table.get_string())

def printRequerimiento6(value, lstSize, lstSizePosicion, posicion):
    print(f"La cantidad de jugadores en la posicion '{posicion}' es: {lstSizePosicion}")
    print(f"La cantidad de jugadores mas similares a el jugador dado son: {lstSize}")
    table = PrettyTable()
    table.field_names = ["Nombre Completo", "Edad", "Nacimiento", "Nacionalidad", "Contrato", "Salarario", "Club", "Liga", "Potencial", "Desempeño", "Posiciones", "Valor Representativo", "Comentarios", "Etiquetas"]
    table.max_table_width = 120
    table.max_width = 20
    
    if lstSize == 1:
        player = lt.getElement(lt.getElement(value, 1), 1)
        table.add_row([player["long_name"],
                       player["age"],
                       player["dob"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["club_name"],
                       player["league_name"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["vr"],
                       player["player_tags"],
                       player["player_traits"]
                       ])
    elif lstSize > 6: 
        for i in range(3):
            for _ in lt.iterator(value):
                    player = lt.getElement(_, 1)
                    table.add_row([player["long_name"],
                            player["age"],
                            player["dob"],
                            player["nationality_name"],
                            player["value_eur"],
                            player["wage_eur"],
                            player["club_name"],
                            player["league_name"],
                            player["potential"],
                            player["overall"],
                            player["player_positions"],
                            player["vr"],
                            player["player_tags"],
                            player["player_traits"]
                            ])
        table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
        table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])
        table.add_row(["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."])

        for _ in range(-1,-4):
                player = lt.getElement(value[_], 1)
                table.add_row([player["long_name"],
                        player["age"],
                        player["dob"],
                        player["nationality_name"],
                        player["value_eur"],
                        player["wage_eur"],
                        player["club_name"],
                        player["league_name"],
                        player["potential"],
                        player["overall"],
                        player["player_positions"],
                        player["vr"],
                        player["player_tags"],
                        player["player_traits"]
                        ])

    else:
        for _ in lt.iterator(value):
            player = lt.getElement(_, 1)
            table.add_row([player["long_name"],
                       player["age"],
                       player["dob"],
                       player["nationality_name"],
                       player["value_eur"],
                       player["wage_eur"],
                       player["club_name"],
                       player["league_name"],
                       player["potential"],
                       player["overall"],
                       player["player_positions"],
                       player["vr"],
                       player["player_tags"],
                       player["player_traits"]
                       ])
    
    return print(table.get_string())

catalog = None
playerAmmount = 0

"""
Menu principal
"""
def menuPrincipal():
    try:
        while True:
            controller.clearConsole()
            printMenu()
            inputs = input('Seleccione una opción para continuar\n> ')
            controller.clearConsole()


            if int(inputs[0]) == 1:
                club = input("Introduzca el club que desea consultar: ")
                matrixDeJugadores, numeroAdquisiciones, ligaALaQuePertenece, tamanioMatrix, league_level  = controller.requerimiento1(catalog, club)
                printRequerimiento1(club, matrixDeJugadores, numeroAdquisiciones, ligaALaQuePertenece, tamanioMatrix, league_level)
                
                input("\n> Hundir cualquier tecla para continuar...")


            elif int(inputs[0]) == 2:
                playerPosition = input("Por favor introducir la posicion de el jugador: ")
                limInferiorDesempenio = float(input("Por favor introducir el limite inferior del desempenio: "))
                limSuperiorDesempenio = float(input("Por favor introducir el limite superior del desempenio: "))
                limInferiorPotencial = float(input("Por favor introducir el limite superior del potencial: "))
                limSuperiorPotencial = float(input("Por favor introducir el limite superior del potencial: "))
                limInferiorSalario = float(input("Por favor introducir el limite superior del salario: "))
                limSuperiorSalario = float(input("Por favor introducir el limite superior del salario: "))
                lstPlayers, lstSize, totalPlayerAmmount = controller.requerimiento2(catalog,
                                                                playerPosition,
                                                                limInferiorDesempenio,
                                                                limSuperiorDesempenio,
                                                                limInferiorPotencial,
                                                                limSuperiorPotencial,
                                                                limInferiorSalario,
                                                                limSuperiorSalario)
                printRequerimiento2(lstPlayers, lstSize, playerPosition, totalPlayerAmmount, limInferiorDesempenio, limSuperiorDesempenio, limInferiorPotencial, limSuperiorPotencial, limInferiorSalario, limSuperiorSalario)
                input("\n> Hundir cualquier tecla para continuar...")
            

            elif int(inputs[0]) == 3:
                playerTag = input("Por favor introducir el tag que desea consultar: ")
                limInferiorSalario = float(input("Por favor introducir el limite superior del salario: "))
                limSuperiorSalario = float(input("Por favor introducir el limite superior del salario: "))
                lstPlayers, lstSize = controller.requerimiento3(catalog, limInferiorSalario, limSuperiorSalario, playerTag)
                printRequerimiento3(lstPlayers, lstSize, playerTag, limInferiorSalario, limSuperiorSalario, playerAmmount)
                input("\n> Hundir cualquier tecla para continuar...")


            elif int(inputs[0]) == 4:

                lim_inf = input("Ingrese el límite inferior de la fecha de nacimiento del jugador: ")
                lim_sup = input("Ingrese el límite superior de la fecha de nacimiento del jugador: ")
                trait = input("Ingrese una de las características que identifican a los jugadores: ")
                lst, size = controller.requerimiento4(catalog, lim_inf, lim_sup, trait)
                printRequerimiento4(lst, size)
                input("\n> Hundir cualquier tecla para continuar...")


            elif int(inputs[0]) == 5:
                propiedad = input("Ingrese la propiedad que desea consultar: ")
                segmentos = int(input("Ingrese cantidad de segmentos (bins) que desea usar: "))
                niveles = int(input("Ingrese la cantidad de niveles que desea usar: "))
                lstSizeJugadores, sizeMapa, razonDeCambio, lstConteo, lstMark, minKey, maxKey = controller.requerimiento5(catalog, segmentos, niveles, propiedad)
                printRequerimiento5(propiedad, segmentos, niveles, lstSizeJugadores, sizeMapa, razonDeCambio, lstConteo, lstMark, minKey, maxKey)
                
                
                input("\n> Hundir cualquier tecla para continuar...")


            elif int(inputs[0]) == 6:
                playerShortName = input("Introduzca el nombre del jugador que desea consultar: ")
                posicion = input("Ingrese la posicion del jugador que desea consultar: ")
                value, lstSize, SizePosicion = controller.requerimiento6(catalog, playerShortName, posicion)
                printRequerimiento6(value, lstSize, SizePosicion, posicion)
                input("\n> Hundir cualquier tecla para continuar...")


            elif int(inputs[0]) == 7:
                fileSize = getFileSize()
                print("Cargando información de los archivos ....")
                start = time.process_time()
                playerAmmount = controller.loadData(catalog, fileSize)
                lstPlayers, lstSize = controller.getPrimerosCinco_UltimosCinco(catalog["listaGeneral_Datos"])
                printPrimerosCinco_UltimosCinco_Players(lstPlayers, lstSize)
                print(time.process_time() - start)
                playerAmmount = playerAmmount
                input("\n>Hundir cualquier numero para continuar...")
            

            elif int(inputs[0]) == 8:
                controller.clearConsole()
                controller.exitProgram()
                

    except Exception as ex:
        controller.clearConsole()
        print("Por favor selecciona una opcion valida")
        print(ex.message)
        input("\n>Hundir cualquier numero para continuar...")
        menuPrincipal()


# ================
# Iniciar programa
# ================
catalog = controller.init()
menuPrincipal()
