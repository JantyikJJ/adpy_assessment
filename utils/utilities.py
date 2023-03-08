import json


class Utilities:
    @staticmethod
    def load_file(filename):
        # Open file, read contents, then return JSON object as a result.
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return json.loads(content)
