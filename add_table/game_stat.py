



class GameStat:
    def __init__(self, cfg):
        self.cfg = cfg
        self.current_level = cfg.current_level

        self.levels = cfg.levels
        self.game_time = 0
        self.place = None

    def calc_rang(self, time):
        for m, interval in self.cfg.grade_to_rang.items():
            if time in range(interval[0], interval[1] + 1):
                return m
        else: return ""


    def __repr__(self):
        return "stat: lev-{}, time-{}, место-{}".format(
            self.current_level, self.game_time, self.place)



