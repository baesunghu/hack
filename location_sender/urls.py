from django.urls import path
from .views import index  # index �Լ��� ����

urlpatterns = [
    path('', index, name='index'),
]
