from falcon import testing
from app import api


class BaseTestCase(testing.TestCase):

    def setUp(self):
        super().setUp()

        self.app = api
        self.auth_header = {"Authorization": "Token 34"}
