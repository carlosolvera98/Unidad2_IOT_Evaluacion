#Login con usuario utng y password mexico -> iniciales_login.py
#Carlos Antonio Suarez Olvera
#GDS0151
def login(u,p):
    ue="utng"
    pe="mexico"

    if u == ue:
        if p == pe:
            print("Bienvenido")
        else:
            print("Password incorrecto")
    else:
        print("Usuario incorrecto")

u=input("Ingresa el usuario: ")
p=input("Ingresa la contrasena: ")
login(u,p)
