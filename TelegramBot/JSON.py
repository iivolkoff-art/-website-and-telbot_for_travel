import json

class JSON:
    def __init__(self):
        self.path = "TelegramBot/last_id.json"

    def get_last_id(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data['id']

    def set_last_id(self, id):
        with open(self.path, "w") as file:
            json.dump({'id': id}, file)
