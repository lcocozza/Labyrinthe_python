class Map:
    """Objet Map"""

    def __init__(self, filename):
        """Initialise l'objet Map"""
        self._map = []
        self._py = 0
        self._px = 0
        self._lastcase = ' '
        with open("map/" + filename, 'r') as file:
            content = file.read()
        map = content.split('\n')
        for line in map:
            self._map.append(list(line))

    def __str__(self):
        """Affiche la map avec print()"""
        return self.to_str(space=True)

    def to_str(self, space=False):
        """Convertie la map en str"""
        map = ""
        for i in range(len(self._map)):
            if space == True:
                map += ' '.join(self._map[i])
            else:
                map += ''.join(self._map[i])
            if i < len(self._map) - 1:
                map += '\n'
        if map[-1] == '\n':
            map = map[:-1]
        return map

    def found_player(self):
        """Cherche le joueur sur la map"""
        for i, line in enumerate(self._map):
            if 'X' in line:
                self.setpyx(i, line.index('X'))
                return (i, line.index('X'))
        return (0, 0)

    def getpy(self):
        """Renvoi la coord y du joueur"""
        return self._py

    def getpx(self):
        """Renvoi la coord x du joueur"""
        return self._px

    def getpyx(self):
        """Renvoi les coords y, x du joueur"""
        return (self._py, self._px)

    def setpy(self, y):
        """Met la coord y du joueur"""
        self._py = y
        return self._py

    def setpx(self, x):
        """Met la coord x du joueur"""
        self._px = x
        return self._px

    def setpyx(self, y, x):
        """Met les coords y, x du joueur"""
        self.setpy(y)
        self.setpx(x)
        return (y, x)

    def move_player(self, y, x):
        """Deplace le joueur sur la carte, d'une coord a un autre"""
        py, px = self.getpyx()
        self._map[py][px] = self._lastcase
        self._lastcase = self._map[y][x]
        py, px = self.setpyx(y, x)
        self._map[py][px] = 'X'

    def move_up(self, nb):
        """Deplace le joueur vers le Nord"""
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y - (i + 1)][x] not in 'OU':
            i += 1
        if self._map[y - (i + 1)][x] == 'U':
            return True
        self.move_player(y - i, x)
        return False

    def move_down(self, nb):
        """Deplace le joueur vers le Sud"""
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y + (i + 1)][x] not in 'OU':
            i += 1
        if self._map[y + (i + 1)][x] == 'U':
            return True
        self.move_player(y + i, x)
        return False

    def move_right(self, nb):
        """deplace le joueur vers l'Est"""
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y][x - (i + 1)] not in 'OU':
            i += 1
        if self._map[y][x - (i + 1)] == 'U':
            return True
        self.move_player(y, x - i)
        return False

    def move_left(self, nb):
        """Deplace le joueur vers L'Ouest"""
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y][x + (i + 1)] not in 'OU':
            i += 1
        if self._map[y][x + (i + 1)] == 'U':
            return True
        self.move_player(y, x + i)
        return False
