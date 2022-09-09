from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView


api_patterns = [
    path('', include('users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
