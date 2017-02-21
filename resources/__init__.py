import falcon


class Index:

    def on_get(self, request, response):
        response.body = 'It works'
