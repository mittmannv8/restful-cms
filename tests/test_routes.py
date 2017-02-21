import json
from tests import BaseTestCase


class RouteTest(BaseTestCase):

    def test_index(self):
        data = self.simulate_get('/', headers=self.auth_header)

        self.assertEqual(data.status_code, 200)

