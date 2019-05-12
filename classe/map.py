class Map:
    """..."""

    def __init__(self, filename):
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
        return self.to_str(space=True)

    def to_str(self, space=False):
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
        for i, line in enumerate(self._map):
            if 'X' in line:
                self.setpyx(i, line.index('X'))
                return (i, line.index('X'))
        return (0, 0)

    def getpy(self):
        return self._py

    def getpx(self):
        return self._px

    def getpyx(self):
        return (self._py, self._px)

    def setpy(self, y):
        self._py = y
        return self._py

    def setpx(self, x):
        self._px = x
        return self._px

    def setpyx(self, y, x):
        self.setpy(y)
        self.setpx(x)
        return (y, x)

    def move_player(self, y, x):
        py, px = self.getpyx()
        self._map[py][px] = self._lastcase
        self._lastcase = self._map[y][x]
        py, px = self.setpyx(y, x)
        self._map[py][px] = 'X'

    def move_up(self, nb):
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y - (i + 1)][x] not in 'OU':
            i += 1
        if self._map[y - (i + 1)][x] == 'U':
            return True
        self.move_player(y - i, x)
        return False

    def move_down(self, nb):
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y + (i + 1)][x] not in 'OU':
            i += 1
        if self._map[y + (i + 1)][x] == 'U':
            return True
        self.move_player(y + i, x)
        return False

    def move_right(self, nb):
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y][x - (i + 1)] not in 'OU':
            i += 1
        if self._map[y][x - (i + 1)] == 'U':
            return True
        self.move_player(y, x - i)
        return False

    def move_left(self, nb):
        i = 0
        y, x = self.getpyx()
        while i < nb and self._map[y][x + (i + 1)] not in 'OU':
            i += 1
        if self._map[y][x + (i + 1)] == 'U':
            return True
        self.move_player(y, x + i)
        return False
