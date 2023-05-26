# FUNCIONES PARA VALIDAR DATOS
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
#FIN FUNCIONES PARA VALIDAR


#INICIO BLOQUE DE FUNCIONES PARA EVITAR DUPLICADOS
def duplicadoRegion(region,lista):### VALIDAMOS QUE LA REGION NO ESTÉ DUPLICADA ✔✔✔✔✔✔✔✔
    while region.upper() in lista:
        region = input("Region repetida, ingresar otra region:")
    return region.upper()
    
def duplicadoValidarPartido(partido,lista):   ### VALIDAMOS QUE NO SE INGRESE PARTIDO REPETIDO O ESPACIO VACÍO✔✔✔✔ 
    while partido.upper() in lista or partido == "":
        partido = input("Partido repetido, ingrese otro partido: ")
    return partido
#FIN BLOQUE DUPLICADOS


### Inicio bloque de codigo para imprimir datos en pantalla

def imprimirDatosPartidos():
    try: archPartidosLectura = open(r"C:\Users\ThinkPad\Desktop\partidosPoliticos.txt","rt")                                                #### ABRIR ARCHIVO 
    except IOError:
        print("No se pudo leer el archivo Partidos")                                                                                    #### EXCEPCIÓN EN CASO DE NO PODER ABRIR ARCHIVO
    else:
        try:
            print("\n\n\n")
            print("________________________________________________________________________")
            print("                          \033[1mPARTIDOS POLITICOS\033[0m        ")
            print("________________________________________________________________________")
            print("       \033[1mNOMBRE\033[0m                 \033[1mABREVIATURA\033[0m                  \033[1mLISTA\033[0m  ")       ###FORMATO DE NEGRITA
            print("________________________________________________________________________")
            for linea in archPartidosLectura:                                                                                           #### ITERAR SOBRE ARCHIVO POR CADA REGISTRO
                nombre,abreviatura,lista = linea.split(";")                                                                             #### SEPARAR VARIABLES DE ARCHIVO CSV CON REFERENCIA DE SEPARADOR ";"
                print("    ""%10s"%nombre,"     ","%15s"%abreviatura,"                ","%10s"%lista,"       ")
                print("________________________________________________________________________")
        finally:
            archPartidosLectura.close()
            

def imprimirDatosRegiones():
    try: archRegionesLectura = open(r"C:\Users\ThinkPad\Desktop\zonaGeografica.txt","rt")                                               ###ARCHIVO PARA LEER
    except IOError:
        print("No se pudo leer el archivo Regiones")                                                                                    ###EXCEPCION EN CASO DE NO PODER ABRIR ARCHIVO
    else:
        try:
            print("\n\n\n")                                                                    #FORMATO DE PRINT
            print("________________________________________________________________________")
            print("                          \033[1mREGIONES GEOGRAFICAS\033[0m        ")
            print("________________________________________________________________________")
            print("                \033[1mNOMBRE\033[0m                      \033[1mCODIGO O ABREVIATURA\033[0m       ")                ###FORMATO DE NEGRITA
            print("________________________________________________________________________")
            for linea in archRegionesLectura:                                                                                           ##### ITERAR POR CADA LINEA DEL ARCHIVO
                region,codigo = linea.split(";")                                                                                        ##### SEPARAR CADA VARIABLE DEL ARCHIVO
                print("        ""%15s"%region,"                            ",codigo,"       ")
                print("________________________________________________________________________")
        finally:
            archRegionesLectura.close()

## Fin bloque para imprimir




##########  PROGRAMA PRINCIPAL  ##############



listaRegiones=[]
listaPartidos=[]

try:
    archPartido = open("/Users/gonzalo/Desktop/partidosPoliticos.csv","wt")        		###CREAMOS EL ARCHIVO DONDE SE ESCRIBIRÁ LA INFO DE PARTIDOS POLITICOS
except IOError:
    print("No se pudo crear el archivo de Partidos")                   							###EXCEPCIÓN EN CASO DE NO PODER CREARLO

else:
    partido = input("Ingrese nombre del partido, FIN para finalizar: ") 			###INGRESAMOS PARTIDO FUERA DE WHILE (CONDICIÓN DE FIN ACÁ)
    partido = duplicadoValidarPartido(partido,listaPartidos)															###VALIDAMOS PARTIDO
    listaPartidos.append(partido.upper())
    while partido.upper() !="FIN":														
        
        abreviatura = input("Ingrese Abreviatura del partido: ")						###INGRESAMOS Y LUEGO VALIDAMOS ABREVIATURA
        validarAbreviatura(abreviatura)
        numeroLista = int(input("Ingresar numero de lista distinto de cero: "))     ###INGRESAMOS Y LUEGO VALIDAMOS NUMERO DE LISTA (ES INT DISTINTO CERO)
        validarNumeroLista(numeroLista)
        archPartido.write(partido.upper()+";"+abreviatura.upper()+";"+str(numeroLista)+"\n")		###PASAMOS LAS 3 VARIABLES AL ARCHIVO YA CREADO Y VOLVEMOS A PEDIR PARTIDO LUEGO
        partido = input("Ingrese nombre del partido, FIN para finalizar: ") 		###VOLVEMOS A PEDIR PARTIDO, PARA REEMPEZAR O TERMINAR CICLO (CONDICIÓN DE FIN ACÁ)
        partido=duplicadoValidarPartido(partido,listaPartidos)
    archPartido.close()															### TERMINADO EL WHILE, CERRAMOS EL ARCHIVO CON LOS CAMBIOS REALIZADOS

contadorRegion = 1                                                            ###CREAMOS UN CONTADOR PARA ASIGNAR A CADA REGION SU CODIGO

try: archRegiones = open("/Users/gonzalo/Desktop/regiones.csv","wt")         ###CREAMOS ARCHIVO PARA REGIONES
except IOError:
    print("No se pudo crear el archivo de Regiones")                         ###CREAMOS EXCEPCION EN CASO DE NO PODER CREARLO
else:
    region = input("Ingrese una region, FIN para finalizar la carga: ")#####    VALIDAR QUE LA REGION NO EXISTA!!!!!!!
    while region.upper() !="FIN":
                              #### SI LA REGION YA EXISTE, PEDIR OTRA AQUÍ, VA UN WHILE
        listaRegiones.append(region.upper())
        archRegiones.write(region.upper()+";"+str(contadorRegion)+"\n")       ### ESCRIBIMOS LA REGION Y EL IDENTIFICADOR EN EL ARCHIVO
        contadorRegion+=1                                             ### AUMENTAMOS EN 1 EL IDENTIFICADOR, PARA LA SIGUIENTE REGION
        region = input("Ingrese una region, FIN para finalizar la carga: ")                        ### INGRESAMOS SIGUIENTE REGION O FINALIZAMOS LA CARGA
        region = duplicadoRegion(region,listaRegiones)

        
    archRegiones.close()                                              ### CERRAMOS EL ARCHIVO DE REGIONES
         

        
#Imprimimos en pantalla los datos ingresados 
imprimirDatosPartidos()
imprimirDatosRegiones()