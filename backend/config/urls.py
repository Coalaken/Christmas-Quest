from django.conf import settings
from django.contrib import admin
from django.urls import path

print(settings.DEBUG)

urlpatterns = [
    path('admin/', admin.site.urls),
]
