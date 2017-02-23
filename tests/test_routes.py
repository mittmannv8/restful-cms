import json
from tests import BaseTestCase


class RouteTest(BaseTestCase):

    def test_index(self):
        data = self.simulate_request('GET', '/')

        self.assertEqual(data.status_code, 200)

    def test_articles_get(self):
        data = self.simulate_request('GET', '/articles/')

        self.assertEqual(data.status_code, 200)

    def test_articles_post(self):
        content = json.dumps({
            'title': 'Title',
            'text': 'Text '*1000,
            'pub_date': '01/01/2001'

        })
        data = self.simulate_request('POST', '/articles/', body=content)

        self.assertEqual(data.status_code, 201)
