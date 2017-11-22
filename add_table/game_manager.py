import collections



class GameManager(collections.MutableMapping):
    def __init__(self, *args, **kwargs):
        self.index = 0
        self.games = {}
        self.games.update(dict(*args, **kwargs))

    def add_game(self, game):
        self.games[self.index] = game
        self.index += 1

    def __getattr__(self, item):
        return self.games[item]

    def __str__(self):
        return str(self.games)

    def __getitem__(self, key):
        return self.games[key]

    def __setitem__(self, key, value):
        self.games[key] = value

    def __delitem__(self, key):
        del self.games[key]

    def __iter__(self):
        return iter(self.games)

    def __len__(self):
        return len(self.games)