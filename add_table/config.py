
from add_table.lib import config_lib

class Config(config_lib.Config):
    def __init__(self, cfg_file):
        self.cfg_file = cfg_file
        self.data = {}
        self._load()


    @property
    def current_game(self):
        return self.data["current_game"]

    @property
    def timer(self):
        return self.data["timer"]

    @property
    def mix(self):
        return self.data["mix"]