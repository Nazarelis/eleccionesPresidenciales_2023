import random
# INICIO BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO
def generarNroDniRandom():
    #GENERA UN NUMERO AL AZAR VALOR ENTERO POSITIVO MENOR A 100000000
    nro = random.randint(0,99999999)
    #NRO PARA EL VOTO EN BLANCO
    if "5" in str(nro):
        print("se encuentra: dni voto en blanco")
    else:
        print("no es un voto en blanco")#EN PROCESO
        
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


# INICIO FUNCIONES DE BUSQUEDAS EN ARCHIVOS

def busquedaRegion(nombreRegion):
    try:                                                                    
        archivoRegiones = open("zonaGeografica.csv", "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        codigoRegion = None
        registro = archivoRegiones.readline()
        while registro:
            nombre, codigo = registro.split(";")
            if nombreRegion == nombre:
                codigoRegion = codigo.rstrip("\n")
                break
            registro = archivoRegiones.readline() 
    finally:
        archivoRegiones.close()
    return codigoRegion

def busquedaPartido(nombrePartido):
    try:                                                                    
        archivoPartido = open("partidosPoliticos.csv", "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        abrevPartido = None
        registro = archivoPartido.readline()
        while registro:
            nombre, abreviatura, codigo = registro.split(";")
            if nombrePartido == nombre:
                abrevPartido = abreviatura
                break
            registro = archivoPartido.readline() 
    finally:
        archivoPartido.close()
    return abrevPartido

# FIN FUNCIONES DE BUSQUEDAS EN ARCHIVOS


# FUNCION PARA OBTENER CODIGO DE REGION                                     
def obtenerCodigoRegion():                                                  
    region = input("Ingrese nombre region a votar: ")
    codigoRegion = busquedaRegion(region.upper())
    while codigoRegion == None:
        print("Region invalida")
        region = input("Reingrese nombre region a votar: ")
        codigoRegion = busquedaRegion(region.upper())
    return codigoRegion.upper()
                                                   
# FIN FUNCION PARA OBTENER CODIGO DE REGION                                 
                                                                            
# FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                               
def obtenerAbreviaturaPartido():
    partido = input("Ingrese nombre partido a votar: ")
    abreviaturaPartido = busquedaPartido(partido.upper())
    while abreviaturaPartido == None:
        print("Partido invalido")
        partido = input("Reingrese nombre partido a votar: ")
        abreviaturaPartido = busquedaPartido(partido.upper())
    return abreviaturaPartido.upper()   
    
    
                                                                            
# FIN FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                          


# FUNCION PARA SELECCIONAR CARGO A VOTAR
def cargoAVotar():
    cargoSeleccionado = input("seleccione cargo a votar: \n [1]. Presidente y Vicepresidente\n [2]. Diputado\n [3]. Senador\n [4]. Gobernador y Vicegobernadr\n ")
    if cargoSeleccionado == "1":
        cargoAVotar = 1
    if cargoSeleccionado == "2":
         cargoAVotar = 2
    if cargoSeleccionado == "3":
         cargoAVotar = 3
    if cargoSeleccionado == "4":
         cargoAVotar = 4
    return cargoAVotar
# FIN FUNCION PARA SELECCIONAR CARGO A VOTAR


##########  PROGRAMA PRINCIPAL  ##########

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
        print(codigoRegion)
        codigoCargo = cargoAVotar()
        print(codigoCargo)
        abrevPartido = obtenerAbreviaturaPartido()
        print(abrevPartido)

        archivoVotos.write(str(dni) + ";" + str(codigoRegion) + ";" + str(codigoCargo) + ";" + abrevPartido + "\n")
finally:
    archivoVotos.close()

# FIN REGISTRO DE VOTOS

##########  FIN PROGRAMA PRINCIPAL  ##########

