from django.urls import path
from .views import receive_location  # index �Լ��� ����

urlpatterns = [
    path('', receive_location, name='receive_location'),
]
