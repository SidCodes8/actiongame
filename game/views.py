"""
Views for the Falling & Catch game.
"""
from django.shortcuts import render
from .game_config import GAME_MODES, GAME_LEVELS, get_game_config
import json


def home_view(request):
    """Landing page for the game."""
    return render(request, 'game/home.html')


def level_select_view(request):
    """Mode and level selection screen."""
    context = {
        'modes': GAME_MODES,
        'levels': GAME_LEVELS,
    }
    return render(request, 'game/level_select.html', context)


def calibration_view(request):
    """Hand tracking calibration screen."""
    return render(request, 'game/calibration.html')


def play_view(request, mode, level):
    """
    Main game screen.
    
    Args:
        mode: Game mode (alphabet, animals, shapes)
        level: Difficulty level (preschool, nursery, kindergarten)
    """
    try:
        config = get_game_config(mode, level)
        
        # Convert config to JSON for JavaScript
        context = {
            'mode': mode,
            'level': level,
            'config_json': json.dumps(config),
            'mode_name': config['mode']['name'],
            'level_name': config['level']['name'],
        }
        
        return render(request, 'game/play.html', context)
    
    except ValueError as e:
        # Invalid mode or level, redirect to level select
        return render(request, 'game/level_select.html', {
            'error': str(e),
            'modes': GAME_MODES,
            'levels': GAME_LEVELS,
        })
