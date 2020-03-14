
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('travello', include('travello.urls')),
    path('admin/', admin.site.urls),
]
