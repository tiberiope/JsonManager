from genericpath import isfile
from json import dump, load

class JsonManager:

    def create_json(self, filepath, *args):
        data = {"username": "", "password": ""}

        if args:
            data = {"username": f"{args[0]}", "password": f"{args[1]}"}

        with open(filepath, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))

    def read_json(self, filepath):
        if isfile(filepath):
            with open(filepath) as f:
                data = load(f)
            return data
        else:
            return False

    def update_json(self, filepath, data):
        with open(filepath, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))
