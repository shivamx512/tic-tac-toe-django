from django.urls import path, include
from .views import GameViewSet
from rest_framework import routers

app_router = routers.DefaultRouter(trailing_slash=False)

app_router.register('game', GameViewSet)

urlpatterns = [
    path('', include(app_router.urls))
]