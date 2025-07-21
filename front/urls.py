from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get_distance/', views.api_get_distance, name='api_get_distance'),
    path("save-var/", views.save_var, name="save_var")
]
