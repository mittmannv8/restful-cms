import falcon
from models import content


class ArticleList:
    """
    Endpoint: /articles/
    """

    def on_get(self, request, response):
        pass

    def on_post(self, request, response):
        article = content.Article(request.json)
        if article.validate():
            response.status = falcon.HTTP_201
        else:
            response.status = falcon.HTTP_400
