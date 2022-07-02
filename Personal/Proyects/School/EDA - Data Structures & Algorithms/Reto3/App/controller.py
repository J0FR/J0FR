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
from datetime import datetime
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# =====================================
# Inicialización del Catálogo de libros
# =====================================
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# ================================
# Funciones para la carga de datos
# ================================
def loadData(catalog, fileName):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    fileName = cf.data_dir + fileName
    input_file = csv.DictReader(open(fileName, encoding="utf-8"),
                                delimiter=",")
    contador = 1
    for player in input_file:
        player["player_positions"] = list(player["player_positions"].replace(",", "").split())
        player["overall"] = float(player["overall"])
        player["potential"] = float(player["potential"])
        player["age"] = float(player["age"])
        player["height_cm"] = float(player["height_cm"])
        player["value_eur"] = 0 if player["value_eur"] == '' else float(player["value_eur"])
        player["club_contract_valid_until"] = datetime.strptime(player["club_contract_valid_until"][0:-2], "%Y")
        player["dob"] = datetime.strptime(player["dob"], "%Y-%m-%d")
        player["wage_eur"] = float(player["wage_eur"])
        player["player_tags"] = list(player["player_tags"].replace(",", "").split()) if len(player["player_tags"]) > 0 else ["Unknown"]
        player["player_traits"] = list(player["player_traits"].replace(", ", ",").split(","))
        model.addPlayer(catalog, player)
        model.addPlayerShortName_playerValue(catalog, player, contador)
        model.clubName_PlayersValue(catalog, player, contador)
        model.posicionJugador_PlayerValue(catalog, player, contador)
        model.playerTag_PlayerValue(catalog, player, contador)
        model.playerAge_playerTraits(catalog, player, contador)

        contador += 1
    playerAmmount = lt.size(catalog["listaGeneral_Datos"])
    return playerAmmount

# =====================
# Funciones de requerimientos
# =====================

def requerimiento1(catalog, club):
    return model.requerimiento1(catalog, club)

def requerimiento2(catalog,
                   playerPosition,
                   limInferiorDesempenio,
                   limSuperiorDesempenio,
                   limInferiorPotencial,
                   limSuperiorPotencial,
                   limInferiorSalario,
                   limSuperiorSalario):
    return model.requerimiento2(catalog,
                   playerPosition,
                   limInferiorDesempenio,
                   limSuperiorDesempenio,
                   limInferiorPotencial,
                   limSuperiorPotencial,
                   limInferiorSalario,
                   limSuperiorSalario)

def requerimiento3(catalog, limInferiorSalario, limSuperiorSalario, playerTag):
    return model.requerimiento3(catalog, limInferiorSalario, limSuperiorSalario, playerTag)

def requerimiento5(catalog, segmentos, niveles, propiedad):
    return model.requerimiento5(catalog, segmentos, niveles, propiedad)

def requerimiento4(catalog, lim_inf, lim_sup, trait):
    lim_inf = datetime.strptime(lim_inf, '%Y-%m-%d')
    lim_sup = datetime.strptime(lim_sup, '%Y-%m-%d')
    return model.requerimiento4(catalog, lim_inf, lim_sup, trait)

def requerimiento6(catalog, playerShortName, posicion):
    return model.requerimiento6(catalog, playerShortName, posicion)

# =====================
# Funciones de consulta
# =====================
def getPrimerosCinco_UltimosCinco(lst):
    return model.getPrimerosCinco_UltimosCinco(lst)

def lstGet(lst, pos):
    return model.lstGet(lst, pos)


# =========================
# Funciones para consola
# =========================
def clearConsole():
    model.clearConsole()

def exitProgram():
    model.exitProgram()