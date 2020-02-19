#Conversion de grados -> iniciales_conversion
#Carlos Antonio Suarez Olvera
#GDS0151

def conversion(a):
    o = ""
    while o != 's':
        o = input("Operacion, c = Celsius, f = Fahrenheit, s = Salir: ")
        if o == 'c':
            print((a * 9/5) + 32)
        elif o == 'f':
            print((a - 32)* 5/9)
        elif o == 's':
            print("Gracias por usar la aplicacion :D ")
        else:
            print("Operacion no valida")
    
a = int(input("Ingresa los grados: "))
conversion(a)
