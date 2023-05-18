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
   

def validarPartido(partido): ####  ✔✔✔ VALIDAMOS QUE EL PARTIDO NO SEA UN CARACTER VACÍO, FUNCIONA ✔ 
    while partido =="":
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

# Programa principal
archivo1=open(r"C:\Users\marilyn\OneDrive\Escritorio\programacion\eleccionesPresidenciales_2023\partidosPoliticos.txt", 'w')
archivo1.write("primer renglón. \n")
archivo1.close()

archivo2=open(r"C:\Users\marilyn\OneDrive\Escritorio\programacion\eleccionesPresidenciales_2023\regionesGeograficas.txt", 'w')
archivo2.write("primer renglón prueba. \n")
archivo2.close()






