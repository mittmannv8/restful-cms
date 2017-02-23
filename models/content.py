

class Article:

    def __init__(self, data):
        self.text = data.get('text', None)
        self.title = data.get('title', None)
        self.pub_date = data.get('pub_date', None)

    def validate(self):
        if not all(self.__dict__.values()):
            return False

        return True

    def save(self):
        pass
