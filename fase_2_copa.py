import random

def buscar_valor(matriz, columna, valor):
    for i in range(len(matriz)):
        if matriz[i][columna] == valor:
            return i
    return -1

def llenarMatriz(filas,columnas,m):
    for i in range(filas):
        m.append([])
        for j in range(columnas):
            m[i].append(0)
    print(m)

def imprimirMatriz(filas,columnas,m):
    print("\n\n        DNI     REGION     PRES       DIP       SEN       GOB  \n")
    for i in range(filas):
        print("\n")
        for j in range(columnas):
            print("%10d"%m[i][j],end="")



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

# FUNCION PARA OBTENER LOS NOMBRES DE REGIONES Y RETORNAR UNA LISTA CON ESOS DATOS
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
# CODIGO REGION RETORNA CON UN .RSTRIP PARA ELIMINAR EL \n Y EVITAR QUE SE HAGAN SALTOS DE PAGINAS POSTERIORMENTE
    return codigoRegion.rstrip("\n")                      
# FIN FUNCION PARA OBTENER CODIGO DE REGION                                 


# FUNCION PARA OBTENER ABREVIATURA DE PARTIDO                               
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


##########  PROGRAMA PRINCIPAL  ##########

listaCargos = ["PRESIDENTE Y VICEPRESIDENTE", "DIPUTADO", "SENADOR", "GOBERNADOR Y VICEGOBERNADOR"]
listaNombreRegiones = obtenerListaDeRegiones()
m=[]

cantidadRegiones = busquedaCantRegistrosEnArchivos("zonaGeografica.csv")
cantidadVotantesRegion = [0]*cantidadRegiones
totalBlancosRegiones=[0]*cantidadRegiones


# INICIO REGISTRO DE VOTOS
try:
    archivoVotos = open("archivo_votacion.csv", "wt")
except IOError as msg:
    print(msg)
else:
    cantidadRegistros = ingresarValidarCantidadRegistros("Indique en números cuántos sufragios se ingresarán ")
    llenarMatriz(cantidadRegistros,6,m)
    contador=0
    while contador<cantidadRegistros:
        dni = generarNroRandom(0, 99999999)
        codigoRegion = obtenerCodigoRegion()
        codigoCargo = random.randint(1, 4)
        abrevPartido = obtenerAbreviaturaPartido()
        if abrevPartido == "Voto en blanco":
            totalBlancosRegiones[int(codigoRegion)-1]+=1
        
        cantidadVotantesRegion[int(codigoRegion)-1]+=1
        
        
        if buscar_valor(m,0,dni)==-1:
            m[contador][0]=dni
            m[contador][1]=int(codigoRegion)
            m[contador][int(codigoCargo+1)]=1
            archivoVotos.write(str(dni) + ";" + str(codigoRegion) + ";" + str(codigoCargo) + ";" + abrevPartido + "\n")
            print(f'Dni: {dni}, codigo region: {codigoRegion}, codigo cargo: {codigoCargo}, abreviatura del partido: {abrevPartido}')
            contador+=1
        else:
            posDni=buscar_valor(m,0,dni)
            print("dni encontrado en pos",posDni)
            if m[posDni][1] !=codigoRegion:
                print("No puede votar en distinta region")  
            else:
                if m[posDni][int(codigoCargo+1)]==1:
                    print("No puede repetir cargo en su voto")
                    
                else:
                    m[posDni][int(codigoCargo+1)]=1
                    archivoVotos.write(str(dni) + ";" + str(codigoRegion) + ";" + str(codigoCargo) + ";" + abrevPartido + "\n")
                    print(f'Dni: {dni}, codigo region: {codigoRegion}, codigo cargo: {codigoCargo}, abreviatura del partido: {abrevPartido}')
                    contador+=1
        
                    

finally:
    archivoVotos.close()
# FIN REGISTRO DE VOTOS


print(listaNombreRegiones)
print(listaCargos)
imprimirMatriz(cantidadRegistros,6,m)

##########  FIN PROGRAMA PRINCIPAL  ##########


print("\n\nCantidad de votantes por region",cantidadVotantesRegion)
totalVotosRegiones = sum(cantidadVotantesRegion)
print("\ntotal de los votos regiones",totalVotosRegiones)
print("\ntotal de votos blancos por regiones",totalBlancosRegiones)



