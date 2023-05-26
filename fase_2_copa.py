import random
# INICIO BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO
def generarNroDniRandom():
    #GENERA UN NUMERO AL AZAR VALOR ENTERO POSITIVO MENOR A 100000000
    nro = random.randint(0,99999999)
    return nro
# FIN BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO


# FUNCION QUE INGRESA Y VALIDA QUE CANTIDAD N DE REGISTROS SEA NUMERO NATURAL VALIDO
def ingresarValidarCantidadRegistros(mensaje):
    error = False
    cantRegistros = None
    while True:
        try:                                                                                               
            cantRegistros = int(input(mensaje))
            while cantRegistros <= 0:
                cantRegistros = int(input("Debes ingresar numero mayor a 0: "))
        except ValueError:
            print("ERROR, se debe ingresar un numero")
            error = True

        if (cantRegistros != None and cantRegistros > 0) or error == False:
            break
    return cantRegistros
# FIN FUNCION PARA VALIDAR CANTIDAD N DE REGISTROS


# FUNCION PARA OBTENER CODIGO DE REGION                                     ###########################################
def obtenerCodigoRegion():                                                  # INICIO DE BLOQUE DE CODIGO EN PROCESO
    try:                                                                    #
        archivoRegiones = open("zonaGeografica.csv", "rt")                  #
    except IOError:                                                         #
        print("No se pudo encontrar archivo")                               #
    else:                                                                   #
        registro = archivoRegiones.readline()                               #
        while registro:                                                     #
            nombre,codigo= registro.split(";")
            region = input("Ingrese nombre region a votar: ")               #
            if region == nombre:                                            #
                codigoRegion = codigo
            else:                                                           #
                print("Nombre de region invalido")                          #
                region = input("Ingrese nombre region a votar: ")           #
            registro = archivoRegiones.readline()                           #
    finally:
        archivoRegiones.close()                                             #
    return codigoRegion                                                     #                                 
# FIN FUNCION PARA OBTENER CODIGO DE REGION                                 #
                                                                            #
# FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                               #
def obtenerCodigoPartido():                                                 
    try:                                                                    #
        archivoPartidos = open("partidosPoliticos.csv", "rt")               #
    except IOError:                                                         #
        print("No se pudo encontrar archivo")                               #
    else:                                                                   #
        registro = archivoPartidos.readline()                               #
        while registro:                                                     #
            nombre, abreviatura, codigo = registro.split(";")               #
            nombrePartido = input("Ingrese nombre partido a votar: ")       #
            if nombrePartido == nombre:                                     #
                abreviaturaPartido = abreviatura                            #
            else:                                                           #
                print("Nombre de partido invalido")                         #
                region = input("Ingrese nombre partido a votar: ")          #
            registro = archivoPartidos.readline()                           #   
    finally:                                                                #
        archivoPartidos.close()                                             #
    return abreviaturaPartido                                               # FIN BLOQUE DE CODIGO EN PROCESO
# FIN FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                           ##################################


# FUNCION PARA SELECCIONAR CARGO A VOTAR
def cargoAVotar(lCargos):
    cargoSeleccionado = input("seleccione cargo a votar: \n [1]. Presidente y Vicepresidente\n [2]. Diputado\n [3]. Senador\n [4]. Gobernador y Vicegobernadr\n ")
    if cargoSeleccionado == "1":
        cargoAVotar = lCargos[0]
    if cargoSeleccionado == "2":
         cargoAVotar = lCargos[1]
    if cargoSeleccionado == "3":
         cargoAVotar = lCargos[2]
    if cargoSeleccionado == "4":
         cargoAVotar = lCargos[3]
    return cargoAVotar
# FIN FUNCION PARA SELECCIONAR CARGO


##########  PROGRAMA PRINCIPAL  ##########
listaCargos = ["PRESIDENTE Y VICEPRESIDENTE", "DIPUTADO", "SENADOR", "GOBERNADOR Y VICEGOBERNADOR"]

# REGISTRO DE VOTOS
try:
    archivoVotos = open("archivo_votacion.csv", "wt")
except IOError as msg:
    print(msg)
else:
    cantidadRegistros = ingresarValidarCantidadRegistros("Indique en números cuántos sufragios se ingresarán ")
    for i in range(cantidadRegistros):
        dni = generarNroDniRandom()
        print(dni)
        codigoRegion = obtenerCodigoRegion()
        cargo = cargoAVotar()
        abrevPartido = obtenerCodigoPartido()

        archivoVotos.write(str(dni) + ";" + codigoRegion + ";" + cargo + ";" + abrevPartido "\n")
finally:
    archivoVotos.close()

# FIN REGISTRO DE VOTOS

##########  FIN PROGRAMA PRINCIPAL  ##########

