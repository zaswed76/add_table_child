



class GameStat:
    def __init__(self, cfg):
        self.cfg = cfg
        self.current_level = cfg.current_level

        self.levels = cfg.levels
        self.game_time = 0

    def __repr__(self):
        return "stat: lev-{}, time-{}".format(self.current_level, self.game_time)



