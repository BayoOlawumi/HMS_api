from django.test import SimpleTestCase
from django.urls import  reverse,resolve


class TestUrls(SimpleTestCase):
    def test_room_managament(self):
        assert 1==1