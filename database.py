import sqlite3
from copy import copy
from collections import namedtuple


class Table:

    def __init__(self, tablename, values):
        self.__tablename__ = tablename
        self.__columns__ = []

        for col, val in values:
            self.__columns__.append(col)
            self.__setattr__(col, val)

    def update(self):
        with Database() as db:
            db.table(self.__tablename__).update(list(self))

    def __iter__(self):
        return iter([(col, getattr(self, col)) for col in self.__columns__])

    def __str__(self):
        return '<Table {}: id({})'.format(self.__tablename__, self.id)

    def __repr__(self):
        return self.__str__()


class Database:

    __imutable_columns__ = ['id']

    def __init__(self):
        # self.connection = sqlite3.connect(':memory:')
        self.connection = sqlite3.connect('db.sqlite')
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.connection.close()
        # pass

    def table(self, table_name):
        this = copy(self)
        this.table_name = table_name
        return this

    def _normalize(self):
        columns = [column[0] for column in self.cursor.description]
        data = self.cursor.fetchall()

        return [Table(self.table_name, zip(columns, values)) for values in data]

        obj = namedtuple(self.table_name.capitalize(), columns)

        return [obj(*values) for values in data]

    def _sqlfy(self, values):
        _id, sets = None, []
        for k, v in values:
            if k == 'id':
                _id = v
                continue
            if k not in self.__imutable_columns__:
                sets.append('{}="{}"'.format(k, v))

        return _id, sets

    def select(self):
        try:
            self.cursor.execute('SELECT * FROM {};'.format(self.table_name))
            return self._normalize()

        except AttributeError:
            return AttributeError('''Table not speccolumns.\n
                User instance.table(str:table_name).select(*args)''')

    def update(self, values):
        _id, sets = self._sqlfy(values)

        if _id:
            self.cursor.execute('UPDATE {} SET {} WHERE id={};'.format(
                self.table_name, ','.join(sets), _id))
            self.connection.commit()

    def insert(self, values):
        if type(values[0]) != 'list':
            columns, values = [(value,) for value in values]
        else:
            columns, values = zip(*values)

        columns = ['"{}"'.format(col) for col in columns]
        values = ['"{}"'.format(val) for val in values]

        query = 'INSERT INTO {} ({}) VALUES ({});'.format(
            self.table_name, ','.join(columns), ','.join(values))

        self.cursor.execute(query)
        self.connection.commit()
