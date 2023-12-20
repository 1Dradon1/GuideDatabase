import json


class Config:
    def __init__(self):
        with open('config.json', 'r') as file:
            json_data = json.load(file)
            self.db_path = json_data['db_path']
            self.program_path = json_data['program_path']
            self.debug = bool(json_data['debug'])
            self.port = json_data['port']