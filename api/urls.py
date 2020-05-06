from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    send_confirmation_code,
    get_user_token,
    UserViewSet,
    UserInfo,
    ReviewsViewSet,
    CommentsViewSet,
    GenreViewSet,
    CategoriesViewSet,
    TitleViewSet,
    ReviewDetailViewSet
)

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet)
v1_router.register('categories', CategoriesViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('titles', TitleViewSet)
v1_router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewDetailViewSet, basename="comment")
v1_router.register('reviews', ReviewsViewSet)
v1_router.register('comments', CommentsViewSet, basename='comments')

urlpatterns = [
        path('v1/auth/email/',  send_confirmation_code),
        path('v1/auth/token/', get_user_token),
        path('v1/users/me/', UserInfo.as_view())
    ]

urlpatterns += [
    path('v1/', include(v1_router.urls)),
]




