#Funcion para IVA -> iniciales_desgloce.py
#Carlos Antonio Suarez Olvera
#GDS0151

def iva(cantidad):
    inicial=cantidad
    ivaTotal=(cantidad*0.16)
    sobrante = (cantidad-ivaTotal)
    print("La cantidad inicial es: $" +str(inicial))
    print("El importe de iva es: $"+str(ivaTotal))
    print("El saldo sobrante es de: $"+str(sobrante))
    
    
cantidad = float(input("Ingresa el capital inicial: $"))
iva(cantidad)
