from django.urls import path
from .views import HomeView, SignUpView, LoginView, SignoutView, GameListView, GameDetailView, board_view_update, GameCreateView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('game/', GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('game_create/', GameCreateView.as_view(), name='game_create'),
    path('game/<int:pk>/board_update/', board_view_update, name='board_update'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', SignoutView.as_view(), name='logout'),
]