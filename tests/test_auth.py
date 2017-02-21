from tests import BaseTestCase


class AuthotizationTestCase(BaseTestCase):

    def test_request_without_authorizarion_header(self):
        request = self.simulate_get('/')

        self.assertEqual(request.status_code, 401)

    def test_request_with_authotization_header(self):
        request = self.simulate_get('/', headers=self.auth_header)

        self.assertEqual(request.status_code, 200)
