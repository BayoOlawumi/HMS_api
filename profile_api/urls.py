from django.conf.urls import url
from django.contrib import admin
from .import views

#app_name='profile_api'
urlpatterns=[
    #Handing profile
    url(r'^$',views.ProfileUser.as_view(),name='profile_user'),
    #url(r'^UserList/', views.JSONResponse, name='UserList')
    url(r'^UserList/$', views.UserProfileList, name='UserList'),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserProfileDetail, name='UserDetail')
]