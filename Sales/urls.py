from django.conf.urls import url
from . import views

"""The URL that handles connects the views with the pages

"""

urlpatterns = [
    url(r'^list/', views.product_list),
    url(r'^details/(?P<pk>[0-9]+)$', views.product_detail)
]