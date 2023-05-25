import random
### INICIO BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO
def nroDni(nro):
    #GENERA UN NUMERO AL AZAR DE 9 DIGITOS
    nro = random.randint(0,100000000)
    return nro

### FIN BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO

### BLOQUE DE CODIGO DE FUNCIONES QUE VALIDAN DATOS INGRESADOS POR TECLADO

# FUNCION GENERICA PARA VALIDAR QUE EL NOMBRE INGRESADO YA SEA DE PARTIDO O ZONA GEOGRAFICA NO SEA STRING VACIO ✔✔
def ingresarValidarNombre(mensaje, mensajeDos):                                                            
    nombre = input(mensaje)                                                                                 
    while nombre == "":
        nombre = input(mensajeDos)
    return nombre

# FUNCION PARA VALIDAR QUE QUE EL DATO SEA ALFANUMERICO ✔✔ 
def ingresarValidarAbreviatura(mensaje):
    abv = input(mensaje) 
    while (abv.isalnum()==False):                                                                          
        abv = input("Abreviatura debe ser un valor alfanumerico, reingresar: ")
    return abv

# FUNCION PARA VALIDAR QUE NUMERO LISTA SEA ENTERO Y DISTINTO DE CERO. MANEJA EXCEPCION VALUE ERROR ✔✔ 
def ingresarValidarNumeroLista(mensaje):
    error = False
    numeroLista = None
    while True:
        try:                                                                                               
            numeroLista = int(input(mensaje))
            while numeroLista == 0:
                numeroLista = int(input("Número igual a cero o invalido, reingresa numero: "))
        except ValueError:
            print("ERROR, se debe ingresar un numero")
            error = True

        if (numeroLista != None and numeroLista != 0) or error == False:
            break
    return numeroLista

### FIN BLOQUE DE CODIGO PARA FUNCIONES QUE VALIDAN DATOS INGRESADOS POR TECLADO


### INICIO BLOQUE DE CODIGO DE FUNCIONES DE BUSQUEDA QUE EVITEN DUPLICADOS

# BUSQUEDA DE NOMBRE DE REGIONES ✔✔✔
def duplicadoRegion(region,lista):                   
    while region.upper() in lista:       
        # SI EL DATO ESTÁ EN LA LISTA SE PIDE OTRO DATO UTILIZANDO LA FUNCION INGRESAR VALIDAR NOMBRE NUEVAMENTE            
        region = ingresarValidarNombre("Region repetida, ingrese otra region: ","Valor vacio, reingrese nombre de region: ") 
    return region.upper()
    
# BUSQUEDA DE NOMBRE DE PARTIDO, SE VERIFICA SI ESTÁ REPETIDO O ES UN ESPACIO VACÍO✔✔✔✔ 
def duplicadoValidarPartido(partido,lista):                                                                
    while partido.upper() in lista or partido == "":                                                       
        partido = ingresarValidarNombre("Partido repetido, ingrese otro: ","Valor vacio, reingrese nombre de partido: ")                               
    return partido.upper()

# BUSQUEDA DE ABREVIATURA DE PARTIDO, SE VERIFICA SI ESTÁ REPETIDO O ES UN ESPACIO VACÍO✔✔✔✔ 
def duplicadoValidarAbreviaturaPartido(abreviatura,lista):                                                 
    while abreviatura.upper() in lista or abreviatura == "":
        abreviatura = ingresarValidarAbreviatura("Partido de abreviatura repetido o erroneo, ingrese otro: ")
    return abreviatura 

# BUSQUEDA DE NÚMERO DE LISTA DE PARTIDO, SE VERIFICA SI ESTÁ REPETIDO O ES UN ESPACIO VACÍO✔✔✔✔ 
def duplicadoValidarNumeroLista(numero,lista):                                                             
    while numero in lista or numero == "":
        numero = ingresarValidarNumeroLista("Número de Lista repetido o erroneo, ingrese otro: ")
    return numero

### FIN BLOQUE DE CODIGO PARA BUSQUEDAS QUE EVITEN DUPLICADOS



### INICIO BLOQUE DE CODIGO PARA IMPRIMIR DATOS EN PANTALLA CON FUNCIONES

def imprimirDatosPartidos():
    try: archPartidosLectura = open("partidosPoliticos.csv", "rt")  # ABRIR ARCHIVO PARA LEER DATOS PARTIDOS
    except IOError:                                                 # EXCEPCIÓN EN CASO DE NO PODER ABRIR ARCHIVO
        print("No se pudo leer el archivo Partidos")                
    else:
        try:
            print("\n\n\n")
            print("________________________________________________________________________")
            print("                          \033[1mPARTIDOS POLITICOS\033[0m        ")
            print("________________________________________________________________________")             # FORMATO DE NEGRITA
            print("       \033[1mNOMBRE\033[0m                 \033[1mABREVIATURA\033[0m                  \033[1mLISTA\033[0m  ")       
            print("________________________________________________________________________")
            for linea in archPartidosLectura:                                                             # ITERAR SOBRE ARCHIVO POR CADA REGISTRO
                nombre,abreviatura,lista = linea.split(";")                                               # SEPARAR VARIABLES DE ARCHIVO CSV CON REFERENCIA DE SEPARADOR ";"
                print("    ""%10s"%nombre,"     ","%15s"%abreviatura,"                ","%10s"%lista,"       ")
                print("________________________________________________________________________")
        finally:
            archPartidosLectura.close()
            

def imprimirDatosRegiones():
    try: archRegionesLectura = open("zonaGeografica.csv", "rt")                      # ABRIR ARCHIVO PARA LEER DATOS REGIONES
    except IOError:
        print("No se pudo leer el archivo Regiones")                                 # EXCEPCION EN CASO DE NO PODER ABRIR ARCHIVO
    else:
        try:
            print("\n\n\n")                                                                                  # FORMATO DE PRINT
            print("________________________________________________________________________")
            print("                          \033[1mREGIONES GEOGRAFICAS\033[0m        ")
            print("________________________________________________________________________")
            print("                \033[1mNOMBRE\033[0m                      \033[1mCODIGO O ABREVIATURA\033[0m       ")     # FORMATO DE NEGRITA
            print("________________________________________________________________________")
            for linea in archRegionesLectura:                                                                                # ITERAR POR CADA LINEA DEL ARCHIVO
                region,codigo = linea.split(";")                                                                             # SEPARAR CADA VARIABLE DEL ARCHIVO
                print("        ""%15s"%region,"                            ",codigo,"       ")
                print("________________________________________________________________________")
        finally:
            archRegionesLectura.close()

### FIN BLOQUE DE FUNCIONES PARA IMPRIMIR DATOS EN PANTALLAS




##########  PROGRAMA PRINCIPAL  ##########


listaRegiones = []
listaPartidos = []
listaAbreviaturas = []
listaDeNumeros = []
# BANDERAS PARA VERIFICAR QUE SE INGRESARON DATOS
ingresoDatosRegiones = False
ingresoDatosPartidos = False

try:
    archPartido = open("partidosPoliticos.csv","at")        		 # CREAMOS EL ARCHIVO DONDE SE ESCRIBIRÁ LA INFO DE PARTIDOS POLITICOS
except IOError:
    print("No se pudo crear el archivo de Partidos")                 # EXCEPCIÓN EN CASO DE NO PODER CREARLO

else:
    partido = ingresarValidarNombre("Ingrese nombre del partido, FIN para finalizar: ","Valor vacio, reingrese nombre de partido: ") 		# INGRESAMOS PARTIDO FUERA DE WHILE (CONDICIÓN DE FIN ACÁ)
    
    while partido.upper() != "FIN":		                                                           # WHILE CON "FIN" COMO CONDICION PARA SALIR. TODOS LOS STRINGS SON CONVERTIDOS EN MAYUSCULAS PARA EVITAR REPETICIONES EN MINUSCULAS 												
        partido=duplicadoValidarPartido(partido,listaPartidos)                                     # VALIDAMOS PARTIDO										
        listaPartidos.append(partido.upper())

        abreviatura = ingresarValidarAbreviatura("Ingrese Abreviatura del partido: ")				# INGRESAMOS Y LUEGO VALIDAMOS ABREVIATURA
        abreviatura = duplicadoValidarAbreviaturaPartido(abreviatura,listaAbreviaturas)
        listaAbreviaturas.append(abreviatura.upper())

        numeroLista = ingresarValidarNumeroLista("Ingresar numero de lista distinto de cero: ")     # INGRESAMOS Y LUEGO VALIDAMOS NUMERO DE LISTA (ES INT DISTINTO CERO)
        numeroLista = duplicadoValidarNumeroLista(numeroLista,listaDeNumeros)
        listaDeNumeros.append(numeroLista)

        
        archPartido.write(partido.upper()+";"+abreviatura.upper()+";"+str(numeroLista)+"\n")		  # ESCRIBIMOS LAS 3 VARIABLES AL ARCHIVO YA CREADO
        ingresoDatosPartidos = True
        partido = ingresarValidarNombre("Ingrese nombre del partido, FIN para finalizar: ","Valor vacio, reingrese nombre de partido: ") # VOLVEMOS A PEDIR PARTIDO, PARA VOLVER A TOMAR MÁS DATOS O TERMINAR EL CICLO (CONDICIÓN DE FIN ACÁ)

    # TERMINADO EL WHILE, CERRAMOS EL ARCHIVO CON LOS CAMBIOS REALIZADOS
    archPartido.close()															                              


# CREAMOS UN CONTADOR PARA ASIGNAR A CADA REGION SU CODIGO
contadorRegion = 1                                                                                            

# CREAMOS ARCHIVO PARA REGIONES
try: archRegiones = open("zonaGeografica.csv","at") 
# CREAMOS EXCEPCION EN CASO DE NO PODER CREARLO                                                          
except IOError:
    print("No se pudo crear el archivo de Regiones")                                                          
else:
    region = ingresarValidarNombre("Ingrese una region, FIN para finalizar la carga: ","Valor vacío, reingrese nombre de region: ")    
    while region.upper() != "FIN":
                                                                                        
        listaRegiones.append(region.upper())
        # ESCRIBIMOS LA REGION Y EL IDENTIFICADOR EN EL ARCHIVO
        archRegiones.write(region.upper() + ";" + str(contadorRegion)+"\n")
        ingresoDatosRegiones = True           
        # AUMENTAMOS EN 1 EL IDENTIFICADOR, PARA LA SIGUIENTE REGION
        contadorRegion += 1                                                             
        # INGRESAMOS SIGUIENTE REGION O FINALIZAMOS LA CARGA
        region = ingresarValidarNombre("Ingrese una region, FIN para finalizar la carga: ","Valor vacío, reingrese nombre de region: ") 
        # SE VERIFICA QUE NO EXISTA DUPLICADO
        region = duplicadoRegion(region,listaRegiones)                    
    
    # CERRAMOS EL ARCHIVO DE REGIONES
    archRegiones.close()                                                   

if ingresoDatosPartidos == True or ingresoDatosRegiones == True:
    # Imprimimos en pantalla los datos ingresados de partidos
    imprimirDatosPartidos()         
    # Imprimimos en pantalla los datos ingresados de regiones
    imprimirDatosRegiones() 
else:
    print("No se ingresaron datos")                                                             
"""
PRUEBA PARA GENERAR EL NRO DE DNI en proceso---
numero=int(input("seleccione 1 para ingresar su DNI: "))
nro= nroDni(numero)
print(nro)
"""

##########  FIN PROGRAMA PRINCIPAL  ##########