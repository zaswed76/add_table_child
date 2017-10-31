
from add_table.lib import config_lib

class Config(config_lib.Config):
    def __init__(self, cfg_file):
        self.cfg_file = cfg_file
        self.data = {}
        self._load()


    @property
    def levels(self):
        return self.data["levels"]

    @property
    def current_level(self):
        return self.data["current_level"]

    @property
    def current_game(self):
        return self.data["current_game"]

    @property
    def timer(self):
        return self.data["timer"]

    @property
    def mix(self):
        return self.data["mix"]
    @property
    def progress_timer(self):
        return self.data["progress_timer"]

    @property
    def progress_timer_checked(self):
        return self.data["progress_timer_checked"]

    @property
    def progress_max(self):
        return self.data["progress_max"]

    @property
    def grade(self):
        return self.data["grade"]

    @grade.setter
    def grade(self, v):
        self.data["grade"] = v

    @property
    def grade_to_timer(self):
        return self.data["grade_to_timer"]

    @progress_timer_checked.setter
    def progress_timer_checked(self, v):
        self.data["progress_timer_checked"] = v

    @property
    def window_title(self):
        return self.data["window_title"]

    @property
    def grade_to_rang(self):
        return self.data["grade_to_rang"]


