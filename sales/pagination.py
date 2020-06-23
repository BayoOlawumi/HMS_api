from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class ProductCategoryListOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class ProductCategoryPagePagination(PageNumberPagination):
    page_size = 1
