#Funcion que solicita una frase y la imprime al reves -> iniciales_reves.py
#Carlos Antonio Suarez Olvera
#GDS0151
def reves(palabra):
    i=0
    reves = ""
    j= len(palabra)-1
    while(i <= j):
        reves = reves + palabra[j]
        j=j-1
    print ( "La palabra alreves es: ", reves)

palabra = input("Ingrese una palabra: " )
reves(palabra)
