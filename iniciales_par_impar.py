#Funcion que me diga si el numero es par o impar -> iniciales_par_impar.py
#Carlos Antonio Suarez Olvera
#GDS0151
def pimpar(num):
    if num == 0:
        print ("El número ingresado es par")
    elif num%2 == 0:
        print ("El numero ingresado es par")
    else:
        print ("El numero ingresado es impar")

num = input("Introduce un número entero: ")
num = int(num)
pimpar(num)
