import re # EXPRESIONES REGULARES
def impresion(nombres,codigos):
    print("________________________________________________________________________")
    print("                          \033[1mREGIONES GEOGRAFICAS\033[0m        ")
    print("________________________________________________________________________")
    print("                \033[1mNOMBRE\033[0m                      \033[1mCODIGO O ABREVIATURA\033[0m       ")
    print("________________________________________________________________________")

   
def impresionDos(partidos,nombres,abv,lista):
    print("________________________________________________________________________")
    print("                          \033[1mPARTIDOS POLITICOS\033[0m        ")
    print("________________________________________________________________________")
    print("       \033[1mNOMBRE\033[0m                 \033[1mABREVIATURA\033[0m                  \033[1mLISTA\033[0m  ")
    print("________________________________________________________________________")
   
# def busqueda(archivo,posDato,valor):
#     for ():
    

def validarPartido(partido): ####  ✔✔✔ VALIDAMOS QUE EL PARTIDO NO SEA UN CARACTER VACÍO, FUNCIONA ✔ 
    while partido == "":
        partido = input("Valor vacío, reingresar partido")
    return partido

def validarAbreviatura(abv):
    while (abv.isalnum()==False): ##✔✔✔✔✔VALIDAMOS QUE EL VALOR SEA ALFANUMERICO, FUNCIONA ✔ ✔ ✔✔ ✔ ✔
        abv = input("Abreviatura debe ser un valor alfanumerico, reingresar")
    return abv

    
def validarNumeroLista(numero): ###✔✔✔ VALIDAMOS NUMEROlista ENTERO DISTINTO DE CERO, FUNCIONA✔ ✔✔ ✔✔ ✔
    while numero ==0:
        numero = int(input("Número igual a cero, reingresa numero: "))
    return numero
    





##########  PROGRAMA PRINCIPAL  ##############



try:
    archPartido = open(r"C:\Users\ThinkPad\Desktop\partidosPoliticos.txt","wt")        			###CREAMOS EL ARCHIVO					
    archPartidoLectura=open(r"C:\Users\ThinkPad\Desktop\partidosPoliticos.txt","rt")
except IOError:
    print("No se pudo encontrar el archivo")                   							###EXCEPCIÓN SI NO PODEMOS CREARLO (REVISAR UBICACION)
else:
    partido = input("Ingrese nombre del partido, FIN para finalizar: ") 			###INGRESAMOS PARTIDO FUERA DE WHILE (CONDICIÓN DE FIN ACÁ)
    validarPartido(partido)															###VALIDAMOS PARTIDO
    while partido !="FIN":														
        
        abreviatura = input("Ingrese Abreviatura del partido: ")						###INGRESAMOS Y LUEGO VALIDAMOS ABREVIATURA
        validarAbreviatura(abreviatura)
        numeroLista = int(input("Ingresar numero de lista distinto de cero: "))     ###INGRESAMOS Y LUEGO VALIDAMOS NUMERO DE LISTA (ES INT DISTINTO CERO)
        validarNumeroLista(numeroLista)
        archPartido.write(partido+";"+abreviatura+";"+str(numeroLista)+"\n")		###PASAMOS LAS 3 VARIABLES AL ARCHIVO YA CREADO Y VOLVEMOS A PEDIR PARTIDO LUEGO
        
        partido = input("Ingrese nombre del partido, FIN para finalizar: ") 		###VOLVEMOS A PEDIR PARTIDO, PARA REEMPEZAR O TERMINAR WHILE (CONDICIÓN DE FIN ACÁ)
        validarPartido(partido)														###VALIDAMOS PARTIDO
    lines = archPartidoLectura.readlines()#PRUEBAS DE CONSULTA EN EL ARCHIVO
    buscarPalabra = "palabra"
    for x in lines:
        buscar =re.search(buscarPalabra,x)
        print(buscar)
    print(lines)

    archPartido.close()	
    archPartidoLectura.close()
    
    														### TERMINADO EL WHILE, CERRAMOS EL ARCHIVO

