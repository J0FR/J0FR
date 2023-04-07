import desmovilizados as mod
import pandas as pd

def ejecutar_cargar_datos()->pd.DataFrame:
    ruta = input("Ingrese el nombre del archivo con la información de los desmovilizados: ")
    resultados = mod.cargar_datos(ruta)
    print("Datos cargados exitosamente!")
    return resultados

def ejecutar_desmovilizados_segun_grupo_armado(datos: pd.DataFrame) -> None:
    mod.desmovilizados_segun_grupo_armado(datos)

def ejecutar_desmovilizados_por_rango_anios(datos: pd.DataFrame) -> None:
    anio_inf = int(input("Ingrese el año inferior: "))
    anio_sup = int(input("Ingrese el año superior: "))
    mod.desmovilizados_por_rango_anios(datos, anio_inf, anio_sup)

def ejecutar_top_departamentos_por_tipo(datos: pd.DataFrame) -> None:
    tipo = input("Ingrese el tipo de desmovilización: ")
    mod.top_departamentos_por_tipo(datos, tipo)

def ejecutar_distribucion_numero_de_hijos_por_sexo(datos: pd.DataFrame) -> None:
    mod.distribucion_numero_de_hijos_por_sexo(datos)

def ejecutar_histograma_por_ocupacion(datos: pd.DataFrame) -> None:
    mod.histograma_por_ocupacion(datos)

def ejecutar_crear_matriz(datos: pd.DataFrame) -> None:
    return mod.crear_matriz(datos)

def ejecutar_desmovilizados_por_departamento(tupla_matriz: tuple) -> None:
    depto = input("Ingrese el nombre del departamento que desea consultar: ")
    grupo = mod.mayor_grupo_por_departamento(tupla_matriz, depto)
    print("El grupo con más desmovilizados en {0} es {1}".format(depto, grupo))

def ejecutar_desmovilizados_por_grupo(tupla_matriz: tuple) -> None:
    grupo = input("Ingrese el nombre del grupo que desea consultar: ")
    numero = mod.desmovilizados_por_grupo(tupla_matriz, grupo)
    print("El número de desmovilizados del grupo {0} es {1}".format(grupo, numero))

def ejecutar_mayor_desmovilizados_grupo_y_departamento(tupla_matriz: tuple) -> None:
    t = mod.mayor_desmovilizados_grupo_y_departamento(tupla_matriz)
    print("El departamento y grupo que tuvo mayor número de desmovilizados fue {0} y {1}".format(t[0], t[1]))
    
def ejecutar_departamentos_mapa(tupla_matriz: tuple) -> None:
    mod.departamentos_mapa(tupla_matriz)

def mostrar_menu()->None:
    print("\nMenú de opciones:")
    print("1. Cargar datos desmovilizados")
    print("2. Ver distribución de los desmovilizados según grupo armado")
    print("3. Ver tendencia del número de desmovilizados por rango de años")
    print("4. Ver top 5 departamentos por tipo de desmovilización")
    print("5. Ver diagrama de caja y bigotes según número de hijos y sexo")
    print("6. Ver ocupación de los individuos que hayan recibiso algún beneficio o desembolso")
    print("7. Crear matriz de departamento vs ex grupo")
    print("8. Consultar el grupo con más desmovilizados por un departamento")
    print("9. Consultar el número de desmovilizados por ex grupo armado")
    print("10. Consultar el departamento y grupo armado con mayor cantidad de desmovilizados")
    print("11. Generar mapa de ex grupo con mayor desmovilización por departamento")
    print("12. Salir")

def iniciar_aplicacion() -> None:
    datos = None
    tupla_matriz = None
    continuar = True
    
    while continuar:
        mostrar_menu()
        
        opcion = int(input("Ingrese la opción que desea ejecutar: "))
        if opcion == 1:
            datos = ejecutar_cargar_datos()
        elif opcion == 2:
            ejecutar_desmovilizados_segun_grupo_armado(datos)
        elif opcion == 3:
            ejecutar_desmovilizados_por_rango_anios(datos)
        elif opcion == 4:
            ejecutar_top_departamentos_por_tipo(datos)
        elif opcion == 5:
            ejecutar_distribucion_numero_de_hijos_por_sexo(datos)
        elif opcion == 6:
            ejecutar_histograma_por_ocupacion(datos)
        elif opcion == 7:
            tupla_matriz = ejecutar_crear_matriz(datos)
        elif opcion == 8:
            ejecutar_desmovilizados_por_departamento(tupla_matriz)
        elif opcion == 9:
            ejecutar_desmovilizados_por_grupo(tupla_matriz)
        elif opcion == 10:
            ejecutar_mayor_desmovilizados_grupo_y_departamento(tupla_matriz)
        elif opcion == 11:
            ejecutar_departamentos_mapa(tupla_matriz)
        elif opcion == 12:
            continuar = False
        else:
            print("Ingresó una opción no válida, por favor elija una de las opciones del menú")

iniciar_aplicacion()
        
    