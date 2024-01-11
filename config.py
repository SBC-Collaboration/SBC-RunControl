import json
import os


class Config:
    """
    Class object to load and save run config files
    """
    path = ""
    config = {}
    run_config = {}
    sipm_config = {}
    caen_config = {}
    cam_config = {}
    dio_config = {}
    acous_config = {}

    def load_config(self, path="config.json"):
        self.path = path
        self.config = json.load(self.path)

    def save_config(self, path="config.json"):
        self.config
        json.dump(self.config, self.path)
