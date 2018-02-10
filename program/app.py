from add_table.lib import config_lib


class Config(config_lib.Config):
    def __init__(self, cfg_file):
        self.cfg_file = cfg_file
        self.data = {}
        self._load()

    @property
    def size_window(self):
        return self.data["size_window"]

    @property
    def btn_size(self):
        return self.data["btn_size"]

    @property
    def tool_height(self):
        return self.data["tool_height"]