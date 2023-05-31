import random

# INICIO FUNCION PARA GENERAR NUMERO RANDOM
def generarNroRandom(limiteInferior, limiteSuperior):
    # GENERA UN NUMERO AL AZAR VALOR ENTERO POSITIVO MENOR A 100000000
    nroRandom = random.randint(limiteInferior, limiteSuperior)
    return nroRandom
# FIN FUNCION PARA GENERAR NUMERO RANDOM

# INICIO FUNCION QUE INGRESA Y VALIDA QUE CANTIDAD N DE REGISTROS SEA NUMERO NATURAL VALIDO
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

# INICIO FUNCION PARA ENCONTRAR CANTIDAD DE REGISTROS EN LOS ARCHIVOS
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

# INICIO FUNCION PARA OBTENER LOS NOMBRES DE REGIONES Y RETORNAR UNA LISTA CON ESOS DATOS
def obtenerListaDeRegiones():
    lista = []
    try:                                                                    
        archivoParaLeer = open("zonaGeografica.csv", "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        registro = archivoParaLeer.readline()
        while registro:
            nombre, codigo = registro.split(";")
            lista.append(nombre)
            registro = archivoParaLeer.readline()
    finally:
        archivoParaLeer.close()
    return lista
# FIN FUNCION PARA OBTENER LOS NOMBRES DE REGIONES
    

# INICIO FUNCION PARA OBTENER CODIGO DE REGION                                     
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
# CODIGO REGION RETORNA CON UN .RSTRIP PARA ELIMINAR EL \n Y EVITAR QUE SE HAGAN SALTOS DE PAGINAS POSTERIORMENTE
    return codigoRegion.rstrip("\n")                      
# FIN FUNCION PARA OBTENER CODIGO DE REGION                                 


# INICIO FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                               
def obtenerAbreviaturaPartido():
    abrevPartido = "Voto en blanco"
# VARIABLE CANTIDAD PARTIDOS GUARDARÁ LA CANTIDAD DE REGISTROS QUE EXISTEN EN EL ARCHIVO
# SIEMPRE SERÁ MAYOR AL NUMERO DEL ULTIMO REGISTRO (YA QUE VAN DEL 0 A N) POR LO QUE SERVIRÁ TAMBIÉN PARA INDICAR UN VOTO EN BLANCO AL AZAR
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


# INICIO FUNCIONES PARA MANEJAR LOS DATOS DE LOS VOTOS EN MATRICES

# FUNCION INICIALIZAR MATRIZ SOLO GENERA LA PRIMERA FILA Y COLUMNAS DE LA MISMA. MAS ADELANTE SE LE AGREGARÁN MÁS FILAS
def inicializarMatriz(columnas):
    matriz = [[0] * columnas]
    return matriz

def busquedaVotanteEnMatriz(matriz, cantFilas, dni, region, cargo):
    votanteExiste = False
    regionDistinta = False
    yaVotoCargo = False
    filaVotante = None
    
    for f in range(0, cantFilas):
        if dni == matriz[f][0]:
            votanteExiste = True
            filaVotante = f
            break
    
    if votanteExiste == True:
        if int(region) != matriz[filaVotante][1]:
            regionDistinta = True
        if matriz[f][cargo + 1] == 1:
            yaVotoCargo = True
    
    return votanteExiste, filaVotante, regionDistinta, yaVotoCargo

# FUNCION PARA MOSTRARNOS QUE DATOS VAN INGRESANDO POR CADA VOTANTE
def imprimirMatriz(filas,columnas,mat):
    print("\n\n        DNI     REGION     PRES       DIP       SEN       GOB  \n")
    for i in range(filas):
        print("\n")
        for j in range(columnas):
            print("%10d"%mat[i][j],end="")

# FIN FUNCIONES PARA MANEJAR LOS DATOS DE LOS VOTOS EN MATRICES


# INICIO FUNCION PARA CONTAR Y MOSTRAR RESULTADOS # INCOMPLETO
def conteoYMuestraDeVotos(listaNombres):
    lista = [0] * len(listaNombres)
    sumadorVotos = 0
    try:
        archivoParaLeer = open("archivo_votacion.csv", "rt")
    except IOError as msg:
        print(msg)
    else:
        registro = archivoParaLeer.readline()
        while registro:
            dni, region, cargo, partido = registro.split(";")
            regionABuscar = region
            sumadorVotos += 1
            #print(sumadorVotos)
            registro = archivoParaLeer.readline()
            

    finally:
        archivoParaLeer.close()
# FIN FUNCION PARA CONTAR Y MOSTRAR RESULTADOS
    


##########  PROGRAMA PRINCIPAL  ##########

listaCargos = ["PRESIDENTE Y VICEPRESIDENTE", "DIPUTADO", "SENADOR", "GOBERNADOR Y VICEGOBERNADOR"]
listaNombreRegiones = obtenerListaDeRegiones()


# INICIO REGISTRO DE VOTOS
cantVotos = 0
cantDniIngresados = 0
try:
    archivoVotos = open("archivo_votacion.csv", "wt")
except IOError as msg:
    print(msg)
else:
    cantidadRegistros = ingresarValidarCantidadRegistros("Indique en números cuántos sufragios se ingresarán ")
    matriz = inicializarMatriz(6)
    while cantVotos < cantidadRegistros:
                                 
        dni = generarNroRandom(0, 99999999)
        codigoRegion = obtenerCodigoRegion()
        codigoCargo = random.randint(1, 4)
        abrevPartido = obtenerAbreviaturaPartido()
        
        votanteExiste, filaVotante, votoRegion, votoCargo = busquedaVotanteEnMatriz(matriz, cantDniIngresados, dni, codigoRegion, codigoCargo)
        
        # if votanteExiste == True:
        if votoRegion == True or votoCargo == True:
            continue
        
        archivoVotos.write(str(dni) + ";" + str(codigoRegion) + ";" + str(codigoCargo) + ";" + abrevPartido + "\n")
        
        if votanteExiste == False:
            # INGRESA FILA A LA MATRIZ A MEDIDA QUE INGRESAN NUEVOS DNI
            matriz.append([0] * 6)
            cantDniIngresados += 1
            matriz[cantDniIngresados][0] = dni
            matriz[cantDniIngresados][1] = int(codigoRegion)
            matriz[cantDniIngresados][int(codigoCargo+1)] = 1
        else:
            matriz[filaVotante][1] = int(codigoRegion)
            matriz[filaVotante][int(codigoCargo+1)] = 1
        cantVotos += 1
        
finally:
    archivoVotos.close()
# FIN REGISTRO DE VOTOS
matriz = matriz[1:]
imprimirMatriz(cantDniIngresados, 6, matriz)
conteoYMuestraDeVotos(listaNombreRegiones)
##########  FIN PROGRAMA PRINCIPAL  ##########