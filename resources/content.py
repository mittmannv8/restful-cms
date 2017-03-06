import falcon

from models import content
from database import Database
from core.serializer import Serializer

db = Database()


class ArticleList:
    """
    Endpoint: /articles/
    """

    def on_get(self, request, response):
        users = db.table('users').select()
        response.body = Serializer(users[0]).data


    def on_post(self, request, response):
        article = content.Article(request.json)
        if article.validate():
            response.status = falcon.HTTP_201
        else:
            response.status = falcon.HTTP_400
