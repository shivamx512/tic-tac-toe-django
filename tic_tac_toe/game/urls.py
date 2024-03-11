from django.urls import path, include
from .views import HomeView, SignUpView, LoginView, SignoutView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', SignoutView.as_view(), name='logout'),
]