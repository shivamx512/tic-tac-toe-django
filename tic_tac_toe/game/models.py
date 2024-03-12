from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS_CHOICES = [
    ("Active", "Active"),
    ("Inactive", "Inactive"),
    ("Completed", "Completed"),
    ("Draw", "Draw"),
]
CELL_CHOICES = (
        ('', 'Empty'),
        ('X', 'X'),
        ('O', 'O'),
    )


class TicTacToeBoard(models.Model):
    # Define fields for each cell of the Tic-Tac-Toe board
    cell_00 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_01 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_02 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_10 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_11 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_12 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_20 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_21 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)
    cell_22 = models.CharField(max_length=1, choices=CELL_CHOICES, default='', blank=True)

    def __str__(self):
        return f" Tic-Tac-Toe Board {self.id}"
    
    def get_cell_by_id(self, cell_id):
        return getattr(self, cell_id)


class Game(models.Model):
    name = models.CharField(max_length=256)
    player_x = models.ForeignKey(User, related_name='games_as_x', on_delete=models.CASCADE)
    player_o = models.ForeignKey(User, related_name='games_as_o', on_delete=models.CASCADE)
    winner = models.ForeignKey(User, related_name='games_won', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')
    board = models.ForeignKey(TicTacToeBoard, related_name='games_board', on_delete=models.CASCADE, null=True, blank=True)
    last_entry_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Move(models.Model):
    game = models.ForeignKey(Game, related_name='moves', on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    row = models.IntegerField()
    col = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Move by {self.player} in game {self.game}"
