import falcon
import json

from resources import Index, auth
from middleware import Token, JSONDecoder

api = falcon.API(middleware=[Token(), JSONDecoder()])

## Routes
api.add_route('/', Index())

# Auth
# api.add_route('/auth/login/', auth.Login())
