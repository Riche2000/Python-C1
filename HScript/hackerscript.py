#Programa broma
import os


def main():
    # w Si el archivo existe o no existe lo sobre escribe o lo crea modo escritura
    # r Requiere que el archivo exista modo lectura
    desktop_path = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
    print(desktop_path)
    a = open(desktop_path + "LEEME.txt", "w")
    a.write("Ya mamaste...")
    a.close()


if __name__ == "__main__":
    main()
