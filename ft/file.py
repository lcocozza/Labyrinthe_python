from classe.map import *

def check_file(filename):
    """Verifie si le fichier existe"""
    exist = True
    try:
        fd_file = open(filename, "r")
    except FileNotFoundError:
        fd_file = open(filename, "w")
        exist = False
    finally:
        fd_file.close()
    return exist

def save_game(map):
    """Sauvegarde la partie en cours"""
    check_file("map/save.txt")
    with open("map/save.txt", "w") as fd_file:
        fd_file.write(map.to_str())
