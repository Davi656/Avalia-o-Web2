from django.urls import path
from . import views

urlpatterns = [
    path('', views.ola),
    path('mes/', views.mes),
    path('acessos/', views.acessos_view),
    path('oversize/', views.oversize),
]