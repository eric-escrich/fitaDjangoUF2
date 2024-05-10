from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('automobils/', views.lista_automobils, name='llista_automobils'),
]