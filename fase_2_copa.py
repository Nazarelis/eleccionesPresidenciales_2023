import random
### INICIO BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO
def generarNroDniRandom():
    #GENERA UN NUMERO AL AZAR VALOR ENTERO POSITIVO MENOR A 100000000
    nro = random.randint(0,99999999)
    return nro

### FIN BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO






### PROGRAMA PRINCIPAL ###


dni = generarNroDniRandom()
#print(dni)


### FIN PROGRAMA PRINCIPAL ###

