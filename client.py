#validar la constraseña de un usuario c/ un maximio de 3 intentos
#entradas                         contraseña interna
#contraseña                       AyPP2019
#salida
#"la contraseña es correcta"
#"agotaste los 3 intentos"
#----------------------------------------------------------------------------------------------------------------------
#Entradas
passw = "AyPP2019"
for i in range (0,3):
    pwd = input("dame la contraseña\n")
    if pwd == passw:
        print ("la contraseña es correcta")


        from socket import socket


        def main():
            s = socket()
            s.connect(("localhost", 6030))

            while True:
                f = open("captura.png", "rb")
                content = f.read(1024)

                while content:
                    s.sendall(content)
                    content = f.read(1024)
                break

            # Se utiliza el caracter de código 1 para indicar
            # al cliente que ya se ha enviado todo el contenido.
            try:
                s.sendall(chr(1))
            except TypeError:
                s.send(bytes(chr(1), "utf-8"))

            # Cerrar y encriptar
            s.close()
            f.close()
            print("Exito")


        if __name__ == "__main__":
            main()
        break

    if i == 2:
        print("agotaste los 3 intentos")
