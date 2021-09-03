import sqlite3


class CommandLineInvocation:
    def __init__(self, workingDir):
        self.workingDir = workingDir
        self.connection = sqlite3.connect('{path}/langbase.sqlite'.format(path=workingDir))
        self.connection.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.connection.cursor()
        self.closeDb = None
        self.execute = self.special_execute
        self.terms = dict()
        self.results = []
        self.attributes = []

    def special_execute(self, query, params=[]):
        self.cursor.execute(query, params)
        self.attributes.append([description[0] for description in self.cursor.description])
        self.results.append(self.cursor.fetchall())

    def mrr(self):
        return self.results[-1:][0]

    def mra(self):
        return self.attributes[-1:][0]


class Matched_Entry:
    def __init__(self, attributes, record):
        self._attributes = attributes
        self._record = record

        self.build_entries()

    def build_entries(self):
        for index, value in enumerate(self._record):
            setattr(self, str(self._attributes[index]), value)
