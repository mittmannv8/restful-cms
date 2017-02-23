from falcon import testing
from app import api


class BaseTestCase(testing.TestCase):

    def setUp(self):
        super().setUp()
        self.app = api

    def simulate_request(self, method, uri, **kwargs):
        headers = kwargs.pop('headers', {})
        headers.update({"Authorization": "Token 34"})
        if method == 'POST':
            headers.update({"Content-Type": "application/json"})

        return super().simulate_request(method, uri, headers=headers, **kwargs)
