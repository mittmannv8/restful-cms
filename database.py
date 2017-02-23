import sqlite3
import config
from copy import copy
from collections import namedtuple


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.connection.close()

    def table(self, table_name):
        this = copy(self)
        this.table_name = table_name
        return this

    def _normalize(self):
        columns = [column[0] for column in self.cursor.description]
        obj = namedtuple(self.table_name.capitalize(), columns)
        data = self.cursor.fetchall()

        return [obj(*values) for values in data]

    def select(self, columns):
        cursor = self.cursor
        try:
            self.cursor.execute(
                 'SELECT {} FROM {};'.format(columns, self.table_name))
            return self._normalize()

        except AttributeError:
            return AttributeError('''Table not speccolumns.\n
                              User instance.table(str:table_name).select(*args)''')

