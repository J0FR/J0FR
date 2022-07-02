import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import os

#Requerimiento 0 - Cargar datos
def cargar_datos(ruta_archivo:str)->pd.DataFrame:
    here = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(here, f'{ruta_archivo}')
    return pd.read_csv(archivo)

def cargar_coordenadas(nombre_archivo:str)->dict:   
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()
    return deptos

def crear_matriz(datos: pd.DataFrame)-> tuple:
    #Creación de los diccionarios con los grupos y departamentos para la matriz
    datos = datos[datos["ExGrupo"]!="SIN DATO"]
    datos = datos[datos["ExGrupo"]!="SIN DATO MINDEFENSA"]
    grupos =sorted(datos["ExGrupo"].unique())
    grupos_dict = dict(list(enumerate(grupos)))
    deptos = sorted(datos["DepartamentoDeResidencia"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    datos = datos[["DepartamentoDeResidencia", "ExGrupo"]]
    #TODO - Crear la matriz
    matriz = np.empty((len(deptos), len(grupos)), int)
    for i in range((len(deptos))):
        depto = dept_dict[i]
        for _ in range(len(grupos)):
            datos_for = datos[(datos["DepartamentoDeResidencia"] == depto) & (datos["ExGrupo"] == grupos_dict[_])]
            if datos_for.empty == True:
                matriz[i][_] = 0
            else:
                matriz[i][_] = datos_for.value_counts()[0]
    
    return (matriz, dept_dict, grupos_dict)
    

def desmovilizados_segun_grupo_armado(datos: pd.DataFrame) -> None:
    datos = datos[(datos["ExGrupo"] != "SIN DATO") & (datos["ExGrupo"] != "SIN DATO MINDEFENSA")]
    
    datos = datos["ExGrupo"]
    datos = datos.value_counts()
    
    total_d = datos.sum()
    datos = datos.div(total_d)
    
    datos.plot(kind="pie")
    
    labels = []
    keys = datos.keys()
    for i in range(len(datos)):
        labels.append(f"{keys[i]}, {'{:.1%}'.format(datos[keys[i]])}")
    
    plt.ylabel('')
    plt.legend( loc='lower left', labels=labels)
    plt.show()
    
def desmovilizados_por_rango_anios(datos: pd.DataFrame, lim_inferior: int, lim_superior: int) -> None:
    anios = list(range(lim_inferior, lim_superior+1))
    datos = datos["AnioDesmovilizacion"].value_counts()
    values = []
    for i in anios:
        values.append(datos[i])
    plt.plot(anios, values)
    plt.xlabel('Año desmovilizacion')
    plt.ylabel('Numero de desmovilizados')
    plt.show()

def top_departamentos_por_tipo(datos: pd.DataFrame, tipo_desmovilizacion: str) -> None:
    datos = datos[(datos["TipoDeDesmovilizacion"] == tipo_desmovilizacion)]
    datos = datos[['DepartamentoDeResidencia']] 
    
    datos = datos.value_counts()
    keys = datos.keys()

    keys_chart = []
    values_chart = []
    i = 4
    while i != -1:
        keys_chart.append(keys[i][0])
        values_chart.append(datos[keys_chart[-1]])
        i -= 1
    
    plt.barh(keys_chart, values_chart, color="blue", left=1)
    plt.ylabel('Departamento de residencia')
    plt.show()

def distribucion_numero_de_hijos_por_sexo(datos: pd.DataFrame) -> None:
    #NumDeHijos
    datos = datos[["Sexo", "NumDeHijos"]]
    datos = datos[(datos["NumDeHijos"] >= 0)]
    datos.boxplot(by ='Sexo', column =['NumDeHijos'], grid=True)
    plt.suptitle('')
    plt.ylabel('Numero de hijos')
    plt.xlabel('Sexo')
    plt.title("Numero de hijos por sexo")
    plt.show()
    
def histograma_por_ocupacion(datos: pd.DataFrame) -> None:
    datos = datos[(datos["DesembolsoBIE"] != "No") | (datos["BeneficioTRV"] != "No") | (datos["BeneficioFA"] != "No") | (datos["BeneficioFPT"] != "No") | (datos["BeneficioPDT"] != "No")]
    datos = datos[["OcupacionEconomica"]]
    keys_grafica = ["Desocupados", "No Aplica", "Ocupados en el sector Formal", "Ocupados en el sector Informal", "Población Económicamente Inactiva"]
    datos = datos.value_counts()
    values_grafica = []
    for i in keys_grafica:
        if datos.get(f"{i}", "fallo") == "fallo":
            values_grafica.append(0)
        else:
            values_grafica.append(datos[i])
    plt.bar(keys_grafica, values_grafica, width=0.5, align="center")
    plt.xticks(rotation='vertical')
    plt.xlabel('Ocupacion Economica')
    plt.show()

def mayor_grupo_por_departamento(datos: tuple, departamento: str) -> str:
    matriz = datos[0]
    dept_dict = datos[1]
    grupos_dict = datos[2]
    posicion_departamento = 0
    while dept_dict[posicion_departamento] != departamento:
            posicion_departamento += 1
    departamento = matriz[posicion_departamento]
    index_mayor_valor = 0
    for i in range(len(departamento)):
        if departamento[index_mayor_valor] < departamento[i]:
            index_mayor_valor = i

    return grupos_dict[index_mayor_valor]
    # Hacer loops limitados y mas eficientes
    
def desmovilizados_por_grupo(datos: tuple, grupo: str) -> int:
    matriz = datos[0]
    grupos_dict = datos[2]
    index_grupo = 0
    total_personas_grupo = 0
    while grupos_dict[index_grupo] != grupo:
        index_grupo += 1
    for i in matriz:
        total_personas_grupo += i[index_grupo]
    
    return total_personas_grupo

def mayor_desmovilizados_grupo_y_departamento(datos: tuple) -> tuple:
    matriz = datos[0]
    dept_dict = datos[1]
    grupos_dict = datos[2]
    posicion_mayor = [0, 0]
    valor_mayor = 0
    for i in range(len(matriz)):
        departamento = matriz[i]
        for _ in range(len(departamento)):
            if matriz[i][_] > valor_mayor:
                posicion_mayor[0] = i
                posicion_mayor[1] = _
                valor_mayor = matriz[i][_]
    return (dept_dict[posicion_mayor[0]], grupos_dict[posicion_mayor[1]])
                

def departamentos_mapa(datos: tuple) -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    mapa = os.path.join(here, 'mapa.png')
    coordenadas = os.path.join(here, 'coordenadas.txt')
    mapa = mpimg.imread(f"{mapa}").tolist()
    diccionario_de_coordenadas = cargar_coordenadas(f"{coordenadas}")
    colores = {"AUC":[1.0,1.0,0.0], "ELN":[1.0,0.0,0.0], "EPL":[1.0,0.0,1.0], "ERG":[0.0,1.0,1.0], "ERP":[0.0,1.0,0.0], "FARC":[1.0, 0.5, 0.50]}
    matriz = datos[0]
    dept_dict = datos[1]
    dict_columns = datos[2]
    
    legends = []
    labels = []
    for i in range(len(dict_columns)):
        legends.append(mpatches.Patch(color = colores[dict_columns[i]], label=dict_columns[i]))
    
    fig, ax = plt.subplots()
    for _ in range(len(dept_dict)):
        departamento = dept_dict[_]
        grupo = mayor_grupo_por_departamento(datos, f"{dept_dict[_]}")
        coordenadas = [diccionario_de_coordenadas[departamento][1], diccionario_de_coordenadas[departamento][0]]
        rect = mpatches.Rectangle(xy=((coordenadas[0]-(13/2)),(coordenadas[1]-(13/2))), width=13, height=13, linewidth=1, color=colores[grupo]) 
        ax.add_patch(rect)

    plt.legend(handles = legends)
    plt.imshow(mapa)
    plt.show()      