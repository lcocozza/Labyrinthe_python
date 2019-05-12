from os import system, name, listdir
from sys import *


def clear():
    """Clear l'ecran"""
    if name == 'nt':
        system("cls")
    else:
        system("clear")


def print_map_list():
    """Affiche la liste des maps (et la save)"""
    print("Labyrinthes existants:")
    map_list = listdir("map")
    for map in map_list:
        print("\t{} - {}".format(map_list.index(map) + 1, map[:-3]))
    return map_list


def print_error(msg):
    """Affiche un message (erreur)"""
    stdout.write("\033[2A")
    print(msg)
    stdout.write("\033[K\033[A")
