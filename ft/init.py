from ft.display import *
from classe.map import *


def init_roboc():
    """Initialise le jeu"""
    clear()
    map_list = print_map_list()
    map_index = get_map(len(map_list))
    map_file = map_list[map_index - 1]
    map = Map(map_file)
    map.found_player()
    return map


def get_map(len_map_list):
    """Demande au joueur la sur quelle map jouer"""
    good = False
    while good is False:
        try:
            map = input("\nEntrez un numéro de labyrinthe pour commencer à jouer: ")
            assert map.isdigit() and (int(map) > 0 and int(map) <= len_map_list)
        except AssertionError:
            print_error("Erreur de saisie.")
        else:
            good = True
    return int(map)
