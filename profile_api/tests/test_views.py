from django.test import  TestCase, Client
from django.urls import reverse
from profile_api.models import UserProfile
import json

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.list_url=reverse('UserList')
    """ def test_userlist_list_GET(self):
        response=self.client.get(self.list_url)
        self.assertEquals(response.status,200)
        self.assertTemplateUsed(response,'profile/Userlist')"""
