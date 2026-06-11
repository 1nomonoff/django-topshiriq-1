
from django.contrib import admin
from django.urls import path
from telefon.views import telefon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('telefon/',telefon)
]
