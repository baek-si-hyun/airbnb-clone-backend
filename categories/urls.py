from django.urls import path
from . import views

# list : 여러개를 한번에 받겠다
# create : 새로운 데이터를 만들겠다
# retrieve : 한개만 검색하겠다
# partial_update : 원래 있던데이터를 수정하겠다.
# delete : 데이터를 삭제하겠다
urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
