from ft.display import *
from ft.file import *
from classe.map import *


def roboc(map):
    """Lance le jeu"""
    end = False
    while end is False:
        clear()
        print(map)
        entry = get_input()
        end = do_entry(map, entry)
        save_game(map)


def get_input():
    """recupere l'input"""
    good = False
    while good is False:
        try:
            entry = input("\n> ").strip().lower().
            assert good_format(entry) is True
        except AssertionError:
            print_error("Erreur de saisie.")
        else:
            good = True
    return entry


def good_format(entry):
    """Verifie si l'input correspond a un bon format"""
    if len(entry) < 1 or len(entry) > 2:
        return False
    if entry[0] not in "qneso":
        return False
    if len(entry) == 2 and entry[1].isdigit() == False:
        return False
    if len(entry) == 2 and entry[0] == 'q':
        return False
    return True


def do_entry(map, entry):
    """Execute les actions en fonction de l'input"""
    if entry == 'q':
        return True
    if len(entry) == 1:
        entry += '1'
    if entry[0] == 'n':
        end = map.move_up(int(entry[1]))
    if entry[0] == 's':
        end = map.move_down(int(entry[1]))
    if entry[0] == 'e':
        end = map.move_left(int(entry[1]))
    if entry[0] == 'o':
        end = map.move_right(int(entry[1]))
    return end
