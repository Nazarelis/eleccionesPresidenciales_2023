# FUNCIONES PARA VALIDAR DATOS
def ingresarValidarNombre(mensaje, mensajeDos):                                                            ####  ✔✔✔ FUNCION GENERICA PARA VALIDAR QUE EL NOMBRE INGRESADO YA SEA 
    nombre = input(mensaje)                                                                                #### PARTIDO O ZONA GEOGRAFICA NO SEA STRING VACIO ✔✔✔
    while nombre == "":
        nombre = input(mensajeDos)
    return nombre

def ingresarValidarAbreviatura(mensaje):
    abv = input(mensaje) 
    while (abv.isalnum()==False):                                                                          ##✔✔✔✔✔VALIDAMOS QUE EL VALOR SEA ALFANUMERICO✔ ✔ ✔✔ ✔ ✔
        abv = input("Abreviatura debe ser un valor alfanumerico, reingresar: ")
    return abv

    
def ingresarValidarNumeroLista(mensaje):
    error= False
    while True:
        try:                                                                                               ###✔✔✔ VALIDAMOS NUMEROlista ENTERO DISTINTO DE CERO✔ ✔✔ ✔✔ ✔
            numeroLista = int(input(mensaje))
            while numeroLista ==0:
                numeroLista = int(input("Número igual a cero o invalido, reingresa numero: "))
        except ValueError:
            print("ERROR, se debe ingresar un numero")
            error = True

        if numeroLista!=0 or error == False:
            break
            
    return numeroLista
#FIN FUNCIONES PARA VALIDAR DATOS


#INICIO BLOQUE DE FUNCIONES PARA EVITAR DUPLICADOS
def duplicadoRegion(region,lista):                                                                         ### BUSQUEDA DE REGION INGRESADA POR TECLADO Y LA LISTA PARA BUSCAR ✔✔✔✔✔✔✔✔
    while region.upper() in lista:                                                                         ## SE VERIFICA SI ESTA EN LA LISTA
        region = ingresarValidarNombre("Region repetida, ingrese otra region: ","Valor vacio, reingrese nombre de region: ") ## SI EL DATO ESTÁ EN LA LISTA SE PIDE OTRO DATO Y SE UTILIZA LA FUNCION INGRESAR VALIDAR NUEVAMENTE
    return region.upper()
    
def duplicadoValidarPartido(partido,lista):                                                                ### BUSQUEDA DE NOMBRE DE PARTIDO INGRESADO POR TECLADO, SE VERIFICA SI ESTÁ REPETIDO O ES UN ESPACIO VACÍO✔✔✔✔ 
    while partido.upper() in lista or partido == "":                                                       
        partido = ingresarValidarNombre("Partido repetido, ingrese otro: ","Valor vacio, reingrese nombre de partido: ")                               
    return partido.upper()

def duplicadoValidarAbreviaturaPartido(abreviatura,lista):                                                 ### BUSQUEDA DE ABREVIATURA DE PARTIDO, SE VERIFICA SI ESTÁ REPETIDO O ES UN ESPACIO VACÍO✔✔✔✔ 
    while abreviatura.upper() in lista or abreviatura == "":
        abreviatura = ingresarValidarAbreviatura("Partido de abreviatura repetido o erroneo, ingrese otro: ")
    return abreviatura 
    
def duplicadoValidarNumeroLista(numero,lista):                                                             ### BUSQUEDA DE NÚMERO DE LISTA DE PARTIDOS, SE VERIFICA SI ESTÁ REPETIDO O ES UN ESPACIO VACÍO✔✔✔✔ 
    while numero in lista or numero == "":
        numero = ingresarValidarNumeroLista("Número de Lista repetido o erroneo, ingrese otro: ")
    return numero
#FIN BLOQUE DUPLICADOS


### Inicio funciones para imprimir datos en pantalla

def imprimirDatosPartidos():
    try: archPartidosLectura = open("partidosPoliticos.csv","rt")                                          #### ABRIR ARCHIVO PARA LEER DATOS PARTIDOS
    except IOError:
        print("No se pudo leer el archivo Partidos")                                                       #### EXCEPCIÓN EN CASO DE NO PODER ABRIR ARCHIVO
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
    try: archRegionesLectura = open("zonaGeografica.csv","rt")                                               ###ABRIR ARCHIVO PARA LEER DATOS REGIONES
    except IOError:
        print("No se pudo leer el archivo Regiones")                                                         ###EXCEPCION EN CASO DE NO PODER ABRIR ARCHIVO
    else:
        try:
            print("\n\n\n")                                                                                  ##FORMATO DE PRINT
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

####### Fin bloque de codigo para imprimir datos en pantalla ########




                                                                ##########  PROGRAMA PRINCIPAL  ##############



listaRegiones=[]
listaPartidos=[]
listaAbreviaturas=[]
listaDeNumeros = []
try:
    archPartido = open("partidosPoliticos.csv","wt")        		                                          ###CREAMOS EL ARCHIVO DONDE SE ESCRIBIRÁ LA INFO DE PARTIDOS POLITICOS
except IOError:
    print("No se pudo crear el archivo de Partidos")                   							              ###EXCEPCIÓN EN CASO DE NO PODER CREARLO

else:
    partido = ingresarValidarNombre("Ingrese nombre del partido, FIN para finalizar: ","Valor vacio, reingrese nombre de partido") 		###INGRESAMOS PARTIDO FUERA DE WHILE (CONDICIÓN DE FIN ACÁ)
    
    while partido.upper() !="FIN":														
        partido=duplicadoValidarPartido(partido,listaPartidos)                                                ###VALIDAMOS PARTIDO										
        listaPartidos.append(partido.upper())

        abreviatura = ingresarValidarAbreviatura("Ingrese Abreviatura del partido: ")						  ###INGRESAMOS Y LUEGO VALIDAMOS ABREVIATURA
        abreviatura = duplicadoValidarAbreviaturaPartido(abreviatura,listaAbreviaturas)
        listaAbreviaturas.append(abreviatura.upper())

        numeroLista = ingresarValidarNumeroLista("Ingresar numero de lista distinto de cero: ")               ###INGRESAMOS Y LUEGO VALIDAMOS NUMERO DE LISTA (ES INT DISTINTO CERO)
        numeroLista = duplicadoValidarNumeroLista(numeroLista,listaDeNumeros)
        listaDeNumeros.append(numeroLista)

        
        archPartido.write(partido.upper()+";"+abreviatura.upper()+";"+str(numeroLista)+"\n")		          ###PASAMOS LAS 3 VARIABLES AL ARCHIVO YA CREADO Y VOLVEMOS A PEDIR PARTIDO LUEGO
        partido = ingresarValidarNombre("Ingrese nombre del partido, FIN para finalizar: ","Valor vacio, reingrese nombre de partido") 		                      ###VOLVEMOS A PEDIR PARTIDO, PARA REEMPEZAR O TERMINAR CICLO (CONDICIÓN DE FIN ACÁ)

    archPartido.close()															                              ### TERMINADO EL WHILE, CERRAMOS EL ARCHIVO CON LOS CAMBIOS REALIZADOS

contadorRegion = 1                                                                                            ###CREAMOS UN CONTADOR PARA ASIGNAR A CADA REGION SU CODIGO

try: archRegiones = open("zonaGeografica.csv","wt")                                                           ###CREAMOS ARCHIVO PARA REGIONES
except IOError:
    print("No se pudo crear el archivo de Regiones")                                                          ###CREAMOS EXCEPCION EN CASO DE NO PODER CREARLO
else:
    region = ingresarValidarNombre("Ingrese una region, FIN para finalizar la carga: ","Valor vacío, reingrese nombre de region")    
    while region.upper() !="FIN":
                                                                                                              #### SI LA REGION YA EXISTE, PEDIR OTRA AQUÍ, VA UN WHILE
        listaRegiones.append(region.upper())
        archRegiones.write(region.upper()+";"+str(contadorRegion)+"\n")                                       ### ESCRIBIMOS LA REGION Y EL IDENTIFICADOR EN EL ARCHIVO
        contadorRegion+=1                                                                                     ### AUMENTAMOS EN 1 EL IDENTIFICADOR, PARA LA SIGUIENTE REGION
        region = ingresarValidarNombre("Ingrese una region, FIN para finalizar la carga: ","Valor vacío, reingrese nombre de region") ### INGRESAMOS SIGUIENTE REGION O FINALIZAMOS LA CARGA
        region = duplicadoRegion(region,listaRegiones)                                                        ### SE VERIFICA QUE NO EXISTA DUPLICADO

        
    archRegiones.close()                                                                                      ### CERRAMOS EL ARCHIVO DE REGIONES


imprimirDatosPartidos()                                                                                       #Imprimimos en pantalla los datos ingresados de partidos
imprimirDatosRegiones()                                                                                       #Imprimimos en pantalla los datos ingresados de regiones




                                                                ##########  FIN PROGRAMA PRINCIPAL  ##############