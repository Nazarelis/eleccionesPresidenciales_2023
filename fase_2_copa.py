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

        if (cantRegistros != None and cantRegistros != 0) or error == False:
            break
    return cantRegistros
# FIN FUNCION PARA VALIDAR CANTIDAD N DE REGISTROS

def nroRegion(nro):
    nro = random.randint(0,7)
    return nro

# FUNCION MENU PARA SELECCIONAR CARGO A VOTAR
def menu(lCargos):
    menu = input("seleccione cargo a votar: \n [1]. Presidente y Vicepresidente\n [2]. Diputado\n [3]. Senador\n [4]. Gobernador y Vicegobernadr\n [s]. Salir \n")
    while menu != "s":
        while menu == "1":
            cargoAVotar = lCargos[0]
        while menu == "2":
            cargoAVotar = lCargos[1]
        while menu == "1":
            cargoAVotar = lCargos[2]
        while menu == "1":
            cargoAVotar = lCargos[3]
    menu = input("seleccione cargo a votar: \n [1]. Presidente y Vicepresidente\n [2]. Diputado\n [3]. Senador\n [4]. Gobernador y Vicegobernadr\n [s]. Salir \n")
# FIN FUNCION MENU 


##########  PROGRAMA PRINCIPAL  ##########
listaCargos = ["Presidente y Vicepresidente", "Diputado", "Senador", "Gobernado y Vicegobernador"]

try:
    archivoVotos = open("archivo_votacion.csv", "wt")
    archivoPartidos = open("partidosPolitivos.csv", "rt")
    archivoRegiones = open("zonaGeografica.csv", "rt")
except IOError as msg:
    print(msg)
else:
    cantidadRegistros = ingresarValidarCantidadRegistros("Indique en números cuántos sufragios se ingresarán ")
    for i in range(cantidadRegistros):
        dni = generarNroDniRandom()
        #print(dni)
        menu(listaCargos)

##########  FIN PROGRAMA PRINCIPAL  ##########

