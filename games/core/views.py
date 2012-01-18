from django.shortcuts import get_object_or_404

from games.core.models import Game
from games.utils.decorators import render_to


@render_to('core/home.html')
def home(request):
    return {
        'games': Game.objects.all(),
    }

@render_to('core/game_details.html')
def game_details(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return {
        'game': game,
        'recent_scores': game.score_set.all().order_by('-play_date')[:10]
    }
