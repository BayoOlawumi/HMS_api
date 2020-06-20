from django.conf.urls import url
from .views import (
    ProductList,
    ProductCategoryList,
    ProductUpdateDelete,
    ProductCategoryUpdateDelete,
)

"""The URL that handles connects the views with the pages

"""

urlpatterns = [
    url(r'^products/$', ProductList.as_view(), name = ProductList.name),
    url(r'^product/(?P<pk>[0-9]+)/$', ProductUpdateDelete.as_view(), name=ProductUpdateDelete.name),

    url(r'^categories/$', ProductCategoryList.as_view(), name=ProductCategoryList.name),
    url(r'^categories/(?P<pk>[0-9]+)/$', ProductCategoryUpdateDelete.as_view(), name=ProductCategoryUpdateDelete.name),

]
