import pprint
import json
import os.path

class Database():
    def __init__(self):
        self.data = {"readers": [], "books": [], "authors": [], "librarians": [], "logbooks": []}
        self.filename = "database.json"

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as infile:
                self.data = json.load(infile)

    def save(self):
        print(self.data)
        with open(self.filename, 'w', encoding='utf-8') as outfile:
            json.dump(self.data, outfile, indent = 4)

    def clearDB(self):
        self.data = {}
        self.save()