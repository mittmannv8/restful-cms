import json


class Serializer:
    def __init__(self, obj):
        self.obj = obj

    def _serialize(self, obj):
        return json.dumps(obj.__dict__)

    @property
    def data(self):
        return self._serialize(self.obj)

