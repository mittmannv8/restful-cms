import falcon
import json


class JSONDecoder:
    def process_resource(self, request, response, resource, params):
        request.json = {}
        content_type = request.content_type

        if content_type is None or 'application/json' not in content_type:
            return

        if request.content_length in (None, 0):
            return

        body = request.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body. A valid JSON document is required')
        try:
            request.json = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON')



class Token:
    """
    Handles access based on Token
    """

    def process_request(self, request, response):
        if not request.auth or request.auth != 'Token 34':
            raise falcon.HTTPUnauthorized()
