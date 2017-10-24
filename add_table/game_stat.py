



class GameStat:
    def __init__(self, stat_cfg):
        self.stat_cfg = stat_cfg
        self.current_level = cfg.current_level

        self.levels = cfg.levels
        self.game_time = 0
        self.place = None

    def __repr__(self):
        return "stat: lev-{}, time-{}, место-{}".format(self.current_level, self.game_time, self.place)



