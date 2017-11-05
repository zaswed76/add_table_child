



class GameStat:
    def __init__(self, cfg):
        self.cfg = cfg
        self.current_level = cfg.current_level

        self.levels = cfg.levels
        self.game_time = 0
        self.place = None


    def calc_rang(self, time):
        for k, v in self.cfg.grade_to_rang.items():
            if time <= v:
                return k
        else: return ""


    def __repr__(self):
        return "stat: lev-{}, time-{}, место-{}".format(
            self.current_level, self.game_time, self.place)



