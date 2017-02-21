import falcon
import json


class Login:
    """
    Handle for endpoint: /auth/login/
    """

    def on_post(self, request, response):

        data = request.json
        if data:
            if data['username'] and data['password']:
                response.body = 'You are logged'
                response.status = falcon.HTTP_200
            else:
                raise falcon.HTTPBadRequest()
        else:
            raise falcon.HTTPBadRequest()
