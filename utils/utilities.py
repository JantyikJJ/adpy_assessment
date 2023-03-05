import json


class Utilities:
    @staticmethod
    def load_file(filename):
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return json.loads(content)
