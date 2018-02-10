



class GameStat:
    def __init__(self, cfg):
        self.cfg = cfg
        self.current_level = cfg.current_level

        self.levels = cfg.levels
        self.game_time = 0
        self.place = None
        self.current_task = None
        self.current_user_answer = None


    def fill_tasks_list(self, task):
        self.tasks_list.append(dict(task=task))

    def calc_rang(self, time, len_tasks):
        n = 0
        f_len_tasks = float(len_tasks)
        for m, sec in enumerate(self.cfg.grade_to_rang, 1):
            f_sec = float(sec)
            start = len_tasks * n
            end = int(round(f_len_tasks * f_sec + 1))
            diapason = range(start, end)
            n += 1
            if time in diapason:
                return m
        else: return ""


    def __repr__(self):
        return "stat: lev-{}, time-{}, место-{}".format(
            self.current_level, self.game_time, self.place)



