from django.urls import path
from .views import borad_update_api_view

urlpatterns = [
    path('board_update/', borad_update_api_view, name='board_api_update'),
]