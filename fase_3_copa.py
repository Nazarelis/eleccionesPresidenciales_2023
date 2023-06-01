import random

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
            lista.append(nombre)
            registro = archivoParaLeer.readline()
    finally:
        archivoParaLeer.close()
    return lista

def formatoImpresion():
    print("\n\n                                  ","<REGION>","                       ")
    print("                            ELECIONNES GENERALES 2023                     \n\n")
    print("Electores habilitados en la region: ","<EL NUMERO IRIA ACA, TOTAL VOTOS REGION>")
    print("              Porcentaje de vottantes: ","<EL PORCENTAJE ACAAA>")
    print("_______________________________________________________________________________________")
    print("       N° LISTA         PARTIDO POLITICO        VOTOS    ")
    
    for i in range(5):
        print("_______________________________________________________________________________________")
        print("<NUMERO DE LISTA>      <NOMBRE PARTIDO>        <CANTIDAD DE VOTOS>     <PORCENTAJE>")

    print("\n\n                                                 VOTOS POSITIVOS: <cantidad> <porcentaje>")
    print("_______________________________________________________________________________________")
    print("                                                 VOTOS EN BLANCO: <cantidad> <porcentaje>")
    print("_______________________________________________________________________________________")
    print("                                                           TOTAL: <cantidad> <porcentaje>")





listaRegiones = obtenerListaDeRegiones()
listaPartidos = obtenerListaDePartidos()
          


print(listaRegiones)
print(listaPartidos)

formatoImpresion()


listaCargos = ["PRESIDENTE Y VICEPRESIDENTE", "DIPUTADO", "SENADOR", "GOBERNADOR Y VICEGOBERNADOR"]




