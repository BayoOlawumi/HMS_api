from django.conf.urls import url
from . import views

api_name = "room_management"
urlpatterns = [
    url(r'^manage/', views.room_managementView.as_view(), name="room_management")
]