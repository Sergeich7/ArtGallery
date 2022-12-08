
import json

from http import HTTPStatus

from rest_framework.test import APITestCase


class TestUsers(APITestCase):

    def test_users(self):
        resp = self.client.post("/api/users/signup/", {
                'username': '111',
                'email': '111@www.eee',
                'password': '1xcvx222d',
            }, format='json', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(resp.content), {'user': 'created'})

        resp = self.client.login(username='111', password='1xcvx222d')
        self.assertTrue(resp)

#    def test_login(self):
#        resp = self.client.post("/api/users/login/", {
#                'username': '111',
#                'password': '1xcvx222d',
#            }, format='json', follow=True)
#        self.assertEqual(resp.status_code, HTTPStatus.OK)
#
#    def test_edit_canngepass_delete(self):
#client = APIClient()
#client.login(username='lauren', password='secret')

#        resp = self.client.post("/api/users/edit/", {
#                'old_password': '1xcvx222d',
#                'new_password1': '222wwweee',
#                'new_password2': '222wwweee',
#            }, format='json')
#        resp = self.client.post("/api/users/edit/", {
#                'email': '222@www.eee',
#            }, format='json', follow=True)
#
#        self.assertEqual(resp.status_code, HTTPStatus.OK)
#        print(json.loads(resp.content))
#        self.assertEqual(json.loads(resp.content), {'user': 'created'})
