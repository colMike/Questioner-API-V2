from .base_test import BaseTest


class TestUser(BaseTest):
    """ Test class for user endpoints """

    def setUp(self):
        super().setUp()

        self.user = {
            'firstname': 'Vincent',
            'lastname': 'Tirgei',
            'username': 'Vinny',
            'email': 'vin@gmail.com',
            'password': 'aanf#244232Y',
            'phonenumber': '0726002063'
        }

    def tearDown(self):
        super().tearDown()

    def test_sign_up_no_data(self):
        """ Test signup with no data sent """

        res = self.client.post('/api/v2/auth/signup')
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data provided')

    def test_sign_up_empty_data(self):
        """ Test sign up sending empty data """

        self.user.clear()

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data provided')

    def test_sign_up_empty_fields(self):
        """ Test sign up empty fields """

        self.user.update({'firstname': ''})

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data provided')

    def test_sign_up_invalid_password(self):
        """ Test sign up with an invalid password """

        self.user.update({'password': 'fdsgfgfj'})

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data provided')

    def test_sign_up_invalid_email(self):
        """ Test sign up with an invalid email """

        self.user.update({'email': 'jggmail.com'})

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data provided')

    def test_sign_up_short_password(self):
        """ Test sign up with a short password """

        self.user.update({'password': 'fdsg'})

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data provided')

    def test_sign_up_successfully(self):
        """ Test sign up successfully """

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'User created successfully')

    def test_sign_up_same_username(self):
        """ Test sign up with same username """

        self.client.post('/api/v2/auth/signup', json=self.user)

        self.user.update({
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'jd@gmail.com'
        })

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 409)
        self.assertEqual(data['status'], 409)
        self.assertEqual(data['message'], 'Username already exists')

    def test_sign_up_same_email(self):
        """ Test sign up with same email """

        self.client.post('/api/v2/auth/signup', json=self.user)

        self.user.update({
            'firstname': 'John',
            'lastname': 'Doe',
            'username': 'jd'
        })

        res = self.client.post('/api/v2/auth/signup', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 409)
        self.assertEqual(data['status'], 409)
        self.assertEqual(data['message'], 'Email already exists')

    def test_login_no_data(self):
        """ Test login with no data provided """

        res = self.client.post('/api/v2/auth/login')
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data provided')

    def test_login_empty_data(self):
        """ Test login with empty data provided """

        self.user.clear()

        res = self.client.post('/api/v2/auth/login', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data provided')

    def test_login_unregistered_user(self):
        """ Test login with unregistered user credentials """

        res = self.client.post('/api/v2/auth/login', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'User not found')

    def test_login_successfully(self):
        """ Test successfull login """

        self.client.post('/api/v2/auth/signup', json=self.user)

        res = self.client.post('/api/v2/auth/login', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'User logged in successfully')

    def test_login_no_username_provided(self):
        """ Test login with no username provided """

        self.client.post('/api/v2/auth/signup', json=self.user)
        self.user.pop('username', None)

        res = self.client.post('/api/v2/auth/login', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid credentials')

    def test_login_invalid_password(self):
        """ Test login with invalid password """

        self.client.post('/api/v2/auth/signup', json=self.user)
        self.user.update({'password': 'asfdgfdngf'})

        res = self.client.post('/api/v2/auth/login', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data provided')

    def test_login_incorrect_password(self):
        """ Test login with invalid password """

        self.client.post('/api/v2/auth/signup', json=self.user)
        self.user.update({'password': 'zdf7#sdfN'})

        res = self.client.post('/api/v2/auth/login', json=self.user)
        data = res.get_json()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['status'], 422)
        self.assertEqual(data['message'], 'Incorrect password')

    def test_refresh_access_token_no_headers(self):
        """ Test refresh access token with no headers provided """

        res = self.client.post('/api/v2/refresh-token')
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], 'Missing Authorization Header')

    def test_refresh_access_token_passing_access_token(self):
        """ Test refresh access token passing access token """

        res = self.client.post('/api/v2/refresh-token', headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], 'Only refresh tokens are allowed')

    def test_refresh_access_token(self):
        """ Test refresh access token successfully"""

        self.headers.update({'Authorization': 'Bearer {}'.format(
            self.refresh_token)})

        res = self.client.post('/api/v2/refresh-token', headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Token refreshed successfully')

    def test_logout_no_access_token(self):
        """ Test logout without access token """

        res = self.client.post('/api/v2/auth/logout')
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], 'Missing Authorization Header')

    def test_logout_passing_refesh_token(self):
        """ Test logout passing refresh token """

        self.headers.update({'Authorization': 'Bearer {}\
        '.format(self.refresh_token)})

        res = self.client.post('/api/v2/auth/logout', headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], 'Only access tokens are allowed')

    def test_logout(self):
        """ Test logout successfully """

        res = self.client.post('/api/v2/auth/logout', headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Logged out successfully')

    def test_logout_revoked_token(self):
        """ Test logout without access token """

        self.client.post('/api/v2/auth/logout', headers=self.headers)

        res = self.client.post('/api/v2/auth/logout', headers=self.headers)
        data = res.get_json()

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], 'Token has been revoked')

    def test_fetch_user_not_created(self):
        """ Test fetch user whose not been created """

        res = self.client.get('/api/v2/profile/4')
        data = res.get_json()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], 'User not found')

    def test_fetch_user(self):
        """ Test fetch user successfully """
        self.client.post('/api/v2/auth/signup', json=self.user)

        res = self.client.get('/api/v2/profile/1')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data']['id'], 1)
