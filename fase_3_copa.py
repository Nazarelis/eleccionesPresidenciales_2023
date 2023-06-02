import random

def generacionArchivosRegiones(regiones,cargos,partidos,m,total):
    try:
        for i in range(len(regiones)):
            for j in range(len(cargos)):
                    archPartido = open(f'{regiones[i]}__{cargos[j]}.txt',"wt")
                    for l in range(len(partidos)):
                        
                        contador=0
                        contadorTotales=0
                        for k in range(total):
                            if m[k][1]==i and m[k][2]==j+1:
                                contadorTotales+=1
                            if m[k][1]==i and m[k][2]==j+1 and m[k][3]==partidos[l]:
                                contador+=1                            
                        if contadorTotales>0:
                            porcentaje = int((contador/contadorTotales)*100)
                        else:
                            porcentaje = 0
                            
                        archPartido.write(partidos[l]+";"+str(i)+";"+str(contador)+";"+str(porcentaje)+"%"+"\n")
    except IOError:
        print("No se pudo crear el archivo de Partidos")
    else:
        archPartido.close()

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
            print(m[i][j],"  ",end="")
            
def pasarMatriz(m):
    try:                                                                    
        archivoParaLeer = open("archivo_votacion.csv", "rt")                  
    except IOError:
        print("No se pudo encontrar archivo")                               
    else:
        contador=0
        registro = archivoParaLeer.readline()
        for registro in archivoParaLeer:
            
            dni,region,cargo,partido = registro.split(";")
            m[contador][0]=int(dni)
            m[contador][1]=int(region)
            m[contador][2]=int(cargo)
            m[contador][3]=partido.rstrip("\n")
            contador+=1
    finally:
        archivoParaLeer.close()



def contarVotosRegion(lista,lista2):
    try:                                                                    
        archivoParaLeer = open("archivo_votacion.csv", "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        registro = archivoParaLeer.readline()
        for registro in archivoParaLeer:
            dni, region,cargo,partido = registro.split(";")
            lista[int(region)-1]+=1
            if partido.rstrip("\n")  == "Voto en blanco":
                lista2[int(region)-1]+=1
    finally:
        archivoParaLeer.close()
    

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


def obtenerListaDePartidos():
    lista = []
    try:                                                                    
        archivoParaLeer = open("PartidosPoliticos.csv", "rt")                  
    except IOError:                                                         
        print("No se pudo encontrar archivo")                               
    else:
        registro = archivoParaLeer.readline()
        while registro:
            nombre, abreviatura,codigo = registro.split(";")
            lista.append(abreviatura)
            registro = archivoParaLeer.readline()
    finally:
        archivoParaLeer.close()
    return lista

def formatoImpresion(regiones,cargos,votosRegion,votosTotal,cargo,m):
    for i in range(len(regiones)):
            porcentaje = int((votosRegion[i]/votosTotal)*100)
            print("\n\n                                  ",regiones[i],"                       ")
            print("                            ELECIONES GENERALES 2023                     \n\n")
            print("                            Categoría: ",cargos[cargo],"                     ")

            print("                   Electores habilitados en la region: ",votosRegion[i])
            print("                           Porcentaje de votantes: ",porcentaje,"%")
            print("_______________________________________________________________________________________")
            print("       N° LISTA         PARTIDO POLITICO        VOTOS    ")
    
    for i in range(3):
        print("_______________________________________________________________________________________")
        print("<NUMERO DE LISTA>      <NOMBRE PARTIDO>        <CANTIDAD DE VOTOS>     <PORCENTAJE>")

    print("\n\n                                                 VOTOS POSITIVOS: <cantidad> <porcentaje>")
    print("_______________________________________________________________________________________")
    print("                                                 VOTOS EN BLANCO: <cantidad> <porcentaje>")
    print("_______________________________________________________________________________________")
    print("                                                           TOTAL: <cantidad> <porcentaje>")




listaCargos = ["PRESIDENTE Y VICEPRESIDENTE", "DIPUTADO", "SENADOR", "GOBERNADOR Y VICEGOBERNADOR"]

listaRegiones = obtenerListaDeRegiones()
listaPartidos = obtenerListaDePartidos()

votosPorRegion = [0]*len(listaRegiones)
votosBlancosRegiones = [0]*len(listaRegiones)



          

contarVotosRegion(votosPorRegion,votosBlancosRegiones)
votosTotal = sum(votosPorRegion)

m = []
llenarMatriz(votosTotal,4,m)
pasarMatriz(m)
##imprimirMatriz(votosTotal,4,m)


print(listaRegiones)
print("blancos por region",votosBlancosRegiones)
print(listaPartidos)
print(votosPorRegion)

print(votosTotal)

generacionArchivosRegiones(listaRegiones,listaCargos,listaPartidos,m,votosTotal)
formatoImpresion(listaRegiones,listaCargos,votosPorRegion,votosTotal,0,m)
print(m)






