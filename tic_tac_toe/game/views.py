from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, LoginForm
from .models import Game, Move, TicTacToeBoard
from .utils import check_winner


# user auth views 
class SignUpView(SuccessMessageMixin, FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/'
    success_message = "Your account has been created successfully. You are now logged in."


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class LoginView(SuccessMessageMixin, FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    success_message = "You have been logged in successfully."


    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
class SignoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = "You have been logged out in successfully."


class HomeView(TemplateView):
    template_name = 'home.html'


class GameListView(ListView):
    template_name = 'game_list.html'
    model = Game
    context_object_name = 'games'


class GameDetailView(DetailView):
    template_name = 'game_detail.html'
    model = Game
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        context['moves'] = Move.objects.filter(game=self.get_object().id)
        return super().get_context_data(**context)


class GameCreateView(CreateView):
    template_name = 'game_create.html'
    model = Game
    fields = ["name", "player_x", "player_o"]
    success_message = "Game created successfully."
    success_url = reverse_lazy('game_list')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.board = TicTacToeBoard.objects.create()
        return super().form_valid(form)


@csrf_exempt
def board_view_update(request, pk):
    """
    Main function to update the game board view
    """
    from django.http import JsonResponse
    game = Game.objects.get(pk=pk)

    cell_id = request.POST.get('cell_id', None)
    if game.status == "Completed":
        data = {'message': "Game is completed, you can't continue"}
        return JsonResponse(data)
    
    if game.last_entry_by == request.user:
        data = {'message': "you are not allowed to play other turn, wait for your turn"}
        return JsonResponse(data)
    
    if not cell_id:
        data = {'message': "Cell id is required"}
        return JsonResponse(data)

    move_performed = False
    cell = game.board.get_cell_by_id(cell_id)
    if cell:
        data = {'message': "you can't overite current value of cell"}
        return JsonResponse(data)

    if request.user == game.player_o:
        setattr(game.board, cell_id, 'O')
        game.board.save()
        game.last_entry_by = request.user
        is_winning_move = check_winner(game.board, 'O')
        move_performed = True

    elif request.user == game.player_x:
        setattr(game.board, cell_id, 'X')
        game.board.save()
        game.last_entry_by = request.user
        is_winning_move = check_winner(game.board, 'X')
        move_performed = True
    else:
        data = {'message': "you are not allowed to play this game"}
        return JsonResponse(data)
        
    if move_performed:
        cell_id = cell_id.split('_')[1]
        Move.objects.create(
            game=game,
            player=request.user,
            row=int(cell_id[1]),
            col=int(cell_id[0]),
        )
        if is_winning_move:
            game.winner = request.user
            game.status = 'Completed'
        game.save()

    data = {'message': 'Value updated successfuly'}
    return JsonResponse(data)
