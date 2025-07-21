from django.urls import path
from .views import receive_location  # index 함수는 없음

urlpatterns = [
    path('', receive_location, name='receive_location'),
]
