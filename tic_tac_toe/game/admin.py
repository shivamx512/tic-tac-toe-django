from django.contrib import admin

from .models import Game, Move, TicTacToeBoard

class GameModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'player_x', 'player_o', 'winner', 'status')
    list_filter = ('winner', 'status')

class MoveModelAdmin(admin.ModelAdmin):
    list_display = ('game', 'player', 'row', 'col', 'timestamp')
    list_filter = ('game', 'player')

admin.site.register(TicTacToeBoard)
admin.site.register(Game, GameModelAdmin)
admin.site.register(Move, MoveModelAdmin)
