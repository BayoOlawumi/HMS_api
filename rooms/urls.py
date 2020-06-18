from django.conf.urls import url
from rooms import views


urlpatterns = [

    url(r'^room-categories/$', views.RoomCategoryList.as_view(), name=views.RoomCategoryList.name),
    url(r'^room-categories/(?P<pk>[0-9]+)$', views.RoomCategoryDetail.as_view(), name=views.RoomCategoryDetail.name),
    url(r'^room-categories/(?P<pk>[0-9]+)/edit/$', views.RoomCategoryUpdate.as_view(),name=views.RoomCategoryUpdate.name),
    url(r'^room-categories/create$', views.RoomCategoryCreate.as_view(), name=views.RoomCategoryCreate.name),

    url(r'^rooms/$', views.RoomList.as_view(), name=views.RoomList.name),
    url(r'^rooms/(?P<pk>[0-9]+)$', views.RoomDetail.as_view(), name=views.RoomDetail.name),

    url(r'^customers/$', views.CustomerList.as_view(), name=views.CustomerList.name),
    url(r'^customers/(?P<pk>[0-9]+)$', views.CustomerDetail.as_view(), name=views.CustomerDetail.name),

    url(r'^invoices/$', views.InvoiceList.as_view(), name=views.InvoiceList.name),
    url(r'^invoices/(?P<pk>[0-9]+)$', views.InvoiceDetail.as_view(), name=views.InvoiceDetail.name),

    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]