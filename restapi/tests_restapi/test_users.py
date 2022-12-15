
import json

from http import HTTPStatus

from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class TestsUsers(APITestCase):

    def test_create_login(self):
        resp = self.client.post("/api/users/signup/", {
                'username': '111',
                'email': '111@www.eee',
                'password': '1xcvx222d',
            }, format='json', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(resp.content), {'user': 'created'})

        resp = self.client.post("/api/users/login/", {'username': '111', 'password': '1xcvx222d'}, follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

        resp = self.client.put("/api/users/edit/", {
                'email': 'new@www.eee',
            }, format='json', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(resp.content), {'user': 'edited'})

        resp = self.client.put("/api/users/changepassword/", {
                'old_password': '1xcvx222d',
                'new_password1': '222dsfsdf',
                'new_password2': '222dsfsdf',
            }, format='json', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(resp.content), {'pass': 'changed'})


        resp = self.client.post("/api/users/login/", {'username': '111', 'password': '222dsfsdf'}, follow=True)
        resp = self.client.delete("/api/users/delete/", format='json', follow=True)
        self.assertEqual(get_user_model().objects.count(), 0)

