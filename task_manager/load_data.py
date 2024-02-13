import json
from os.path import dirname, join


def from_json(file_name):
    with open(join(dirname(__file__), 'fixtures', file_name)) as file:
        return json.load(file)
