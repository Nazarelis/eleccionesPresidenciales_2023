import random

# INICIO BLOQUE DE CODIGO DE FUNCIONES 
def generarNroRandom(limiteInferior, limiteSuperior):
    # GENERA UN NUMERO AL AZAR VALOR ENTERO POSITIVO MENOR A 100000000
    nroRandom = random.randint(limiteInferior, limiteSuperior)
    return nroRandom
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

# FUNCION PARA ENCONTRAR CANTIDAD DE REGISTROS EN LOS ARCHIVOS
def busquedaCantRegistrosEnArchivos(archivo):
    try:                                                                    
        archivoParaLeer = open(archivo, "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        registros = archivoParaLeer.readlines()
        cantRegistros = len(registros)
    finally:
        archivoParaLeer.close()
    return cantRegistros
# FIN FUNCION PARA ENCONTRAR CANTIDAD DE REGISTROS EN LOS ARCHIVOS

# FUNCION PARA OBTENER CODIGO DE REGION                                     
def obtenerCodigoRegion():                                    
    cantRegiones = busquedaCantRegistrosEnArchivos("zonaGeografica.csv")
    regionAleatoria = random.randint(0,cantRegiones-1)
    try:                                                                    
        archivoParaLeer = open("zonaGeografica.csv", "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        registros = archivoParaLeer.readlines()
        registroAlAzar = registros[regionAleatoria]
        nombreRegion, codigoRegion = registroAlAzar.split(";")
    finally:
        archivoParaLeer.close()
    return codigoRegion.rstrip("\n")
                                                   
# # FIN FUNCION PARA OBTENER CODIGO DE REGION                                 
                                                                            
# FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                               
def obtenerAbreviaturaPartido():
    abrevPartido = "Voto en blanco"
# CANTIDAD PARTIDOS SERA LA CANTIDAD DE REGISTROS QUE EXISTEN EN EL ARCHIVO
# SIEMPRE SERÁ MAYOR AL NUMERO DE REGISTROS POR LO QUE SERVIRÁ TAMBIÉN PARA INDICAR QUE SERÁ UN VOTO EN BLANCO
    cantPartidos = busquedaCantRegistrosEnArchivos("partidosPoliticos.csv")
    partidoAleatorio = random.randint(0,cantPartidos)
    if partidoAleatorio != cantPartidos:
        try:                                                                    
            archivoParaLeer = open("partidosPoliticos.csv", "rt")                  
        except IOError:                                                         
            print("No se pudo encontrar archivo")                               
        else:
            registros = archivoParaLeer.readlines()
            registroAlAzar = registros[partidoAleatorio]
            nombrePartido, abreviaturaPartido, codigoPartido = registroAlAzar.split(";")
            abrevPartido = abreviaturaPartido
        finally:
            archivoParaLeer.close()
    return abrevPartido
                                                                     
# FIN FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                          

def busquedaDeVotante(votante, region):
    yaVoto = False
    try:                                                                    
        archivoParaLeer = open("archivo_votacion.csv", "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        registro = archivoParaLeer.readline()
        while registro:
            dni, codReg, codCargo, abrevPart = registro.split(";")

            if dni == votante:
                yaVoto = True
                print("dni: ", votante, " region: ", codReg, "AAAAAAAAAAcargo votado: ", codCargo)
    return

##########  PROGRAMA PRINCIPAL  ##########

# REGISTRO DE VOTOS
try:
    archivoVotos = open("archivo_votacion.csv", "wt")
except IOError as msg:
    print(msg)
else:
    cantidadRegistros = ingresarValidarCantidadRegistros("Indique en números cuántos sufragios se ingresarán ")
    for i in range(cantidadRegistros):
        dni = generarNroRandom(0, 99999999)
        codigoRegion = obtenerCodigoRegion()
        busquedaDeVotante(dni, codigoRegion)

        codigoCargo = random.randint(1,4)
        abrevPartido = obtenerAbreviaturaPartido()

        archivoVotos.write(str(dni) + ";" + str(codigoRegion) + ";" + str(codigoCargo) + ";" + abrevPartido + "\n")
        print(f'Dni: {dni}, codigo region: {codigoRegion}, codigo cargo: {codigoCargo}, abreviatura del partido: {abrevPartido}')
finally:
    archivoVotos.close()

# FIN REGISTRO DE VOTOS

##########  FIN PROGRAMA PRINCIPAL  ##########



