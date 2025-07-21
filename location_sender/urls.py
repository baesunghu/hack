from django.urls import path
from .views import index  # index 함수는 없음

urlpatterns = [
    path('', index, name='index'),
]
