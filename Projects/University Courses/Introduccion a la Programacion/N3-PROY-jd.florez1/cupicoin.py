def cargar_blockchain_cupicoin(archivo: str) -> list:
    """Funcion que recibe el nombre de un archivo con cierta estructura y organiza los datos de la menera solicitada en el PDF

    Args:
        archivo (str): Nombre del archivo al cual se le quiere tratar los datos

    Returns:
        list: Lista en la estructura solicitada (lista de diccionarios y dentro de estos diccionarios otros diccionarios que representan las transacciones)
    """
    BlockChain_Cupicoin = []
    archivo = open(archivo, "r")
    encabezados = archivo.readline().strip()
    bloque_comprimido = archivo.readline().strip()
    bloque_comprimido_split = bloque_comprimido.split(",")
    bloque_pasado = bloque_comprimido.split(",")
    if not BlockChain_Cupicoin:
            BlockChain_Cupicoin.append({
                "numero_bloque": int(bloque_comprimido_split[1]),
                "cantidad_transacciones": 0,
                "timestamp": None,
                "abierto": True,
                "hash": None, 
                "hash_anterior": None
                })
    
    while bloque_comprimido != "": 
        bloque_comprimido_split = bloque_comprimido.split(",")
        if BlockChain_Cupicoin:
            if int(bloque_pasado[5]) != int(bloque_comprimido_split[5]):
                agregar_nuevo_bloque(BlockChain_Cupicoin, bloque_pasado[5])
            agregar_transaccion(BlockChain_Cupicoin, {
                "codigo_transaccion": bloque_comprimido_split[0],
                "remitente": bloque_comprimido_split[2],
                "destinatario": bloque_comprimido_split[3],
                "valor": float(bloque_comprimido_split[4]),
                "operacion": ("contrato" if bloque_comprimido_split[3] == "" else "transferencia")
            })
        bloque_pasado = bloque_comprimido.split(",")
        bloque_comprimido = archivo.readline().strip()
        bloque_comprimido_split = bloque_comprimido.split(",")

    archivo.close()
    return BlockChain_Cupicoin

def agregar_transaccion(BlockChain: list, transaccion: dict) -> None:
    """Agrega una transaccion en el ultimo bloque del BlockChain

    Args:
        BlockChain (list): Lista de diccionarios que representa el BlockChain
        transaccion (dict): Diccionario el cual trae todos los datos de la transaccion para ser agregada
    """
    BlockChain[-1][BlockChain[-1]["cantidad_transacciones"]] = transaccion
    BlockChain[-1]["cantidad_transacciones"] += 1
    
def agregar_nuevo_bloque(BlockChain: list, timestamp: float) -> None:
    """Crea un nuevo bloque al final y cierra el que estaba abierto anteriormente

    Args:
        BlockChain (list): Lista de diccionarios que representa el BlockChain
        timestamp (int): Es un número que indica el momento en que se ingresó la última transacción del bloque y se calculó el hash del bloque.
    """
    diccionario_final = BlockChain[-1]
    diccionario_final["timestamp"] = float(timestamp)
    diccionario_final["abierto"] = False
    diccionario_final["hash"] =  hash(BlockChain[-1], timestamp)
    BlockChain.append({
        "numero_bloque": int(diccionario_final["numero_bloque"])+1,
        "cantidad_transacciones": 0,
        "timestamp": None,
        "abierto": True,
        "hash": None, 
        "hash_anterior": diccionario_final["hash"]
    })
    
# HALLAR EL HASH
def hash(Bloque: dict, timestamp: float) -> int:
    """Funcion la cual por medio de los argumentos que recibe devuelve el hash del bloque dado

    Args:
        Bloque (dict): Bloque el cual se le quiere sacar el hash
        timestamp (int): Es un número que indica el momento en que se ingresó la última transacción del bloque y se calculó el hash del bloque

    Returns:
        int: Numero del hash, el cual es un valor numérico que es el resultado de aplicar la función de hash al contenido del bloque
    """
    i = 0
    datos_concatenados = ""
    SumaASCII = 0
    
    if Bloque["timestamp"] == None:
        return None
    
    x = True
    while x != False:
        if Bloque.get(i, "error") == "error":
            x = False
        else:
            diccionario_transaccion = Bloque[i]
            datos_concatenados += (diccionario_transaccion["codigo_transaccion"]+diccionario_transaccion["remitente"]+diccionario_transaccion["destinatario"]+str(diccionario_transaccion["valor"])+diccionario_transaccion["operacion"])
        i += 1
    
    datos_concatenados += str(Bloque["numero_bloque"])+("" if str(Bloque["hash_anterior"]) == "None" else str(Bloque["hash_anterior"]))
    
    for _ in datos_concatenados:
        SumaASCII += ord(_)
        
    return float(SumaASCII % float(timestamp))

def contar_veces_aparece_cuenta(BlockChain: list, direccion_de_cuenta: str) -> dict:
    """Cuenta en cuantas transacciones hace parte la cuenta dada en el BlockChain dado

    Args:
        BlockChain (list): Lista de diccionarios que representa el BlockChain
        direccion_de_cuenta (str): string la cual representa la direccion o id de la cuenta

    Returns:
        dict: diccionario con llaves "remitente" y "destinatario" con sus respectivos valores los cuales son la cantidad de veces que participa en cada uno de estos tipos de transacciones
    """
    transacciones = {
        "remitente": 0,
        "destinatario": 0
    }
    for _ in BlockChain:
        i = 0
        while i < (_["cantidad_transacciones"]):
            if _[i]["remitente"] == direccion_de_cuenta:
                transacciones["remitente"] += 1
            elif _[i]["destinatario"] == direccion_de_cuenta:
                transacciones["destinatario"] += 1
            i += 1
    return transacciones

def buscar_transaccion(BlockChain: list, codigo_de_transaccion: str) -> dict:
    """Funcion que busca dentro del BlockChain la transaccion que coincida el codigo de trasaccion dado con el del BlockChain

    Args:
        BlockChain (list): (list): Lista de diccionarios que representa el BlockChain
        codigo_de_transaccion (str): String con codigo de transaccion que se quiere buscar

    Returns:
        dict: Diccionario que es la transaccion con toda su informacion
    """
    for _ in BlockChain:
        i = 0
        while i < (_["cantidad_transacciones"]):
            if _[i]["codigo_transaccion"] == codigo_de_transaccion:
                return _[i]
            i += 1
    else:
        return None
    
def dar_transacciones_entre(BlockChain: list, direccion_remitente: str, direccion_destinatario: str) -> list:
    """Funcion que busca las transacciones entre un remitente y un destinatario dados dentro del BlockChain

    Args:
        BlockChain (list): Lista de diccionarios que representa el BlockChain
        direccion_remitente (str): Direccion o id de la cuenta que funcionaria como remitente
        direccion_destinatario (str): Direccion o id de la cuenta que funcionaria como destinatario

    Returns:
        list: Lista de diccionarios y cada diccionario es una transaccion que cumple lo solicitado
    """
    lista_transacciones = []
    for _ in BlockChain:
        i = 0
        while i < (_["cantidad_transacciones"]):
            if (_[i]["remitente"] == direccion_remitente) and (_[i]["destinatario"] == direccion_destinatario):
                lista_transacciones.append(_[i])
            i += 1
    
    return lista_transacciones
    

def dar_transferencia_mayor_valor(BlockChain: list) -> dict: # revisar
    """Funcion que busca la transferencia de mayor valor en el BlockChain

    Args:
        BlockChain (list): Lista de diccionarios que representa el BlockChain

    Returns:
        dict: diccionario con toda la informacion de la trasaccion de mayor valor
    """
    maximo = BlockChain[0][0]
    for _ in BlockChain:
        i = 0
        while i < (_["cantidad_transacciones"]):
            if maximo["valor"] < _[i]["valor"] and _[i]["operacion"] == "transferencia":
                maximo = _[i]
            
            i += 1
    return maximo

def calcular_saldo_cuenta(BlockChain: list, direccion_de_cuenta: str) -> float:
    """Funcion que calcula el saldo de una cuenta solicitada dentro del BlockChain

    Args:
        BlockChain (list): Lista de diccionarios que representa el BlockChain
        direccion_de_cuenta (str): Direccion o cuenta la cual se le quiere buscar el saldo

    Returns:
        float: Numero decimal que muestra el saldo de la cuenta solicitada
    """
    dinero = 0
    for _ in BlockChain:
        i = 0
        while i < (_["cantidad_transacciones"]):
            if ((_[i]["destinatario"] == direccion_de_cuenta) and (_[i]["operacion"] == "transferencia")) or (_[i]["operacion"] == "contrato"):
                dinero += _[i]["valor"]
            elif (_[i]["remitente"] == direccion_de_cuenta) and (_[i]["operacion"] == "transferencia"):
                dinero -= _[i]["valor"]
            i += 1
    return dinero

def validar_bloque(BlockChain: list) -> bool:
    """Funcion que valida si el BlockChain esta bien o a sido externamente modificado

    Args:
        BlockChain (list): Lista de diccionarios que representa el BlockChain

    Returns:
        bool: bool que retorna True si fue modificado y false si no fue modificado
    """
    for _ in BlockChain:
        if ((_["abierto"] == True) and (_["numero_bloque"] != BlockChain[-1]["numero_bloque"])) or (BlockChain[-1]["abierto"] != True):
            return False
        if (_["hash_anterior"] != BlockChain[_["numero_bloque"]-1]["hash"]):
            return False 
        if hash(_,_["timestamp"]) != _["hash"]:
            return False
    else:
        return True