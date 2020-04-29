from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import send_confirmation_code, get_user_token, UserViewSet, UserInfo, UserInfoViewSet

v1_router = DefaultRouter()
#v1_router.register('users/me', UserInfoViewSet, basename='user info')
v1_router.register('users', UserViewSet)



urlpatterns = [
        path('v1/auth/email/',  send_confirmation_code),
        path('v1/auth/token/', get_user_token),
        path('v1/users/me/', UserInfo.as_view())
    ]
urlpatterns += [
    path('v1/', include(v1_router.urls)),
]




