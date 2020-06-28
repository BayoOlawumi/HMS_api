from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class ProductCategoryListOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 3


class ProductCategoryPagePagination(PageNumberPagination):
    page_size = 3
