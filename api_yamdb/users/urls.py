from django.urls import include, path
from rest_framework import routers

from .views import SignupViewSet, TokenViewSet, UserViewSet

app_name = 'users'

v1_router_auth = routers.DefaultRouter()
v1_router_auth.register(
    'signup', SignupViewSet, basename='signup'
)
v1_router_auth.register(
    'token', TokenViewSet, basename='token'
)


v1_router_users = routers.DefaultRouter()
v1_router_users.register(
    'users', UserViewSet, basename='users'
)

v1_patterns = [
    path('auth/', include(v1_router_auth.urls)),
    path('', include(v1_router_users.urls)),
]

urlpatterns = [
    path('v1', include(v1_patterns)),
]
