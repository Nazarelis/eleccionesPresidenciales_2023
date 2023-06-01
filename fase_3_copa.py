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


listaRegiones = obtenerListaDeRegiones()
listaPartidos = obtenerListaDePartidos()

print(listaRegiones)
print(listaPartidos)




listaCargos = ["PRESIDENTE Y VICEPRESIDENTE", "DIPUTADO", "SENADOR", "GOBERNADOR Y VICEGOBERNADOR"]


