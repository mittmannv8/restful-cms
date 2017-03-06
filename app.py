import falcon
import json

from resources import Index, auth, content, admin
from middleware import Token, JSONDecoder

api = falcon.API(middleware=[JSONDecoder()])

## Routes
api.add_route('/', Index())

# Auth
# api.add_route('/auth/login/', auth.Login())

# Articles
api.add_route('/articles/', content.ArticleList())

# Admin interface
api.add_route('/html/', admin.HTMLTest())

