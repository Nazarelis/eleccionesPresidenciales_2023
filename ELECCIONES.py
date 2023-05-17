def impresionRegiones(nombres,codigos):
    print("________________________________________________________________________")
    print("                          \033[1mREGIONES GEOGRAFICAS\033[0m        ")
    print("________________________________________________________________________")
    print("                \033[1mNOMBRE\033[0m                      \033[1mCODIGO O ABREVIATURA\033[0m       ")
    print("________________________________________________________________________")

   
def impresionPartidos(partidos,nombres,abv,lista):
    print("________________________________________________________________________")
    print("                          \033[1mPARTIDOS POLITICOS\033[0m        ")
    print("________________________________________________________________________")
    print("       \033[1mNOMBRE\033[0m                 \033[1mABREVIATURA\033[0m                  \033[1mLISTA\033[0m  ")
    print("________________________________________________________________________")
   

def validarPartido(partido): ####✔ ✔ ✔ VALIDAMOS QUE EL PARTIDO NO SEA UN CARACTER VACÍO, FUNCIONA ✔ 
    while partido =="":
        partido = input("Valor vacío, reingresar partido")
    return partido

def validarAbreviatura(abv):
    while (abv.isalnum()==False): ##✗✗✗VALIDAMOS QUE EL VALOR SEA ALFANUMERICO, NO FUNCIONA!!!!! ✗✗
        abv = input("Abreviatura debe ser un valor alfanumerico, reingresar")
    return abv

#def validarNumerolista(numero) ###VALIDAMOS QUE EL NUMERO DE LA LISTA SEA UN VALOR ARBITRARIO DISTINTO DE CERO
    







