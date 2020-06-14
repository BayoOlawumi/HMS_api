from django.test import SimpleTestCase
from django.urls import reverse,resolve
from profile_api.views import UserProfileList,UserProfileDetail,ProfileUser

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolves(self):
        url=reverse('UserList')
        self.assertEquals(resolve(url).func,UserProfileList)

    def test_profile_url_is_resolves(self):
        url = reverse('profile_user')
        self.assertEquals(resolve(url).func.view_class, ProfileUser)

    def test_detail_url_is_resolves(self):
        url = reverse('UserDetail',args=[2])
        self.assertEquals(resolve(url).func,UserProfileDetail)