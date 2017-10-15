import json

class Config:
    def __init__(self, cfg_file):
        self.cfg_file = cfg_file
        self.data = {}
        self._load()



    def _load(self):
        with open(self.cfg_file, "r") as f:
            self.data.update(json.load(f))

    def save(self):
        with open(self.cfg_file, 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    @property
    def current_game(self):
        return self.data["current_game"]

    @property
    def timer(self):
        return self.data["timer"]

    @property
    def mix(self):
        return self.data["mix"]