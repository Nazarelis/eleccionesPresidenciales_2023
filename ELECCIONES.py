def impresion(archivo):
    
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
    archPartido = open("/Users/gonzalo/Desktop/partidosPoliticos.csv","wt")        		###CREAMOS EL ARCHIVO DONDE SE ESCRIBIRÁ LA INFO DE PARTIDOS POLITICOS
except IOError:
    print("No se pudo crear el archivo de Partidos")                   							###EXCEPCIÓN EN CASO DE NO PODER CREARLO
else:
    partido = input("Ingrese nombre del partido, FIN para finalizar: ") 			###INGRESAMOS PARTIDO FUERA DE WHILE (CONDICIÓN DE FIN ACÁ)
    validarPartido(partido)															###VALIDAMOS PARTIDO
    while partido !="FIN":														
        
        abreviatura = input("Ingrese Abreviatura del partido: ")						###INGRESAMOS Y LUEGO VALIDAMOS ABREVIATURA
        validarAbreviatura(abreviatura)
        numeroLista = int(input("Ingresar numero de lista distinto de cero: "))     ###INGRESAMOS Y LUEGO VALIDAMOS NUMERO DE LISTA (ES INT DISTINTO CERO)
        validarNumeroLista(numeroLista)
        archPartido.write(partido+";"+abreviatura+";"+str(numeroLista)+"\n")		###PASAMOS LAS 3 VARIABLES AL ARCHIVO YA CREADO Y VOLVEMOS A PEDIR PARTIDO LUEGO
        
        partido = input("Ingrese nombre del partido, FIN para finalizar: ") 		###VOLVEMOS A PEDIR PARTIDO, PARA REEMPEZAR O TERMINAR CICLO (CONDICIÓN DE FIN ACÁ)
        validarPartido(partido)														###VALIDAMOS PARTIDO
    
    archPartido.close()															### TERMINADO EL WHILE, CERRAMOS EL ARCHIVO CON LOS CAMBIOS REALIZADOS


contadorRegion = 1                                                            ###CREAMOS UN CONTADOR PARA ASIGNAR A CADA REGION SU CODIGO

try: archRegiones = open("/Users/gonzalo/Desktop/regiones.csv","wt")         ###CREAMOS ARCHIVO PARA REGIONES
except IOError:
    print("No se pudo crear el archivo de Regiones")                         ###CREAMOS EXCEPCION EN CASO DE NO PODER CREARLO
else:
    region = input("Ingrese una region, FIN para finalizar la carga: ") #####    VALIDAR QUE LA REGION NO EXISTA!!!!!!!
    while region !="FIN":
                              #### SI LA REGION YA EXISTE, PEDIR OTRA AQUÍ, VA UN WHILE
        archRegiones.write(region+";"+str(contadorRegion)+"\n")       ### ESCRIBIMOS LA REGION Y EL IDENTIFICADOR EN EL ARCHIVO
        contadorRegion+=1                                             ### AUMENTAMOS EN 1 EL IDENTIFICADOR, PARA LA SIGUIENTE REGION
        region = input("Ingrese una region, FIN para finalizar la carga: ")                        ### INGRESAMOS SIGUIENTE REGION O FINALIZAMOS LA CARGA
    
    archRegiones.close()                                              ### CERRAMOS EL ARCHIVO DE REGIONES
         

try: archRegionesLectura = open("/Users/gonzalo/Desktop/regiones.csv","rt")
except IOError:
    print("No se pudo leer el archivo Regiones")
else:
    try:
        print("\n\n\n")
        print("________________________________________________________________________")
        print("                          \033[1mREGIONES GEOGRAFICAS\033[0m        ")
        print("________________________________________________________________________")
        print("                \033[1mNOMBRE\033[0m                      \033[1mCODIGO O ABREVIATURA\033[0m       ")
        print("________________________________________________________________________")
        for linea in archRegionesLectura:
            region,codigo = linea.split(";")
            print("        ""%15s"%region,"                            ",codigo,"       ")
            print("________________________________________________________________________")
    finally:
        archRegionesLectura.close()


try: archPartidosLectura = open("/Users/gonzalo/Desktop/partidosPoliticos.csv","rt")
except IOError:
    print("No se pudo leer el archivo Partidos")
else:
    try:
        print("\n\n\n")
        print("________________________________________________________________________")
        print("                          \033[1mPARTIDOS POLITICOS\033[0m        ")
        print("________________________________________________________________________")
        print("       \033[1mNOMBRE\033[0m                 \033[1mABREVIATURA\033[0m                  \033[1mLISTA\033[0m  ")
        print("________________________________________________________________________")
        for linea in archPartidosLectura:
            nombre,abreviatura,lista = linea.split(";")
            print("    ""%10s"%nombre,"     ","%15s"%abreviatura,"     ","%5s"%lista,"       ")
            print("________________________________________________________________________")
    finally:
        archPartidosLectura.close()
