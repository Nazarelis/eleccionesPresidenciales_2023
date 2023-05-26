import random
### INICIO BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO
def nroDni(nro):
    #GENERA UN NUMERO AL AZAR VALOR ENTERO POSITIVO MENOR A 100000000
    nro = random.randint(0,99999999)
    return nro

### FIN BLOQUE DE CODIGO DE FUNCIONES DE REGISTRO


"""
PRUEBA PARA GENERAR EL NRO DE DNI en proceso---
numero=int(input("seleccione 1 para ingresar su DNI: "))
nro= nroDni(numero)
print(nro)
"""