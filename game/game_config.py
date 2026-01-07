"""
Game configuration data for Falling & Catch game.
Defines the 3 modes (Alphabet, Animals, Shapes) and 3 levels (Preschool, Nursery, Kindergarten).
Updated with differentiated learning objectives per level.
"""

# Phonics mapping for Kindergarten Alphabet level
PHONICS_MAP = {
    'A': '/ay/', 'B': '/buh/', 'C': '/kuh/', 'D': '/duh/',
    'E': '/ee/', 'F': '/fuh/', 'G': '/guh/', 'H': '/huh/',
    'I': '/eye/', 'J': '/juh/', 'K': '/kuh/', 'L': '/luh/',
    'M': '/muh/', 'N': '/nuh/', 'O': '/oh/', 'P': '/puh/',
    'Q': '/kwuh/', 'R': '/ruh/', 'S': '/suh/', 'T': '/tuh/',
    'U': '/yoo/', 'V': '/vuh/', 'W': '/wuh/', 'X': '/ks/',
    'Y': '/yuh/', 'Z': '/zuh/'
}

# Animal data with riddles
ANIMALS_DATA = {
    '🐶': {'name': 'Dog', 'riddle': 'the animal that barks', 'sound': 'woof woof'},
    '🐱': {'name': 'Cat', 'riddle': 'the animal that meows', 'sound': 'meow meow'},
    '🦁': {'name': 'Lion', 'riddle': 'the king of the jungle', 'sound': 'roar'},
    '🐘': {'name': 'Elephant', 'riddle': 'the animal with a long trunk', 'sound': 'trumpet'},
    '🐦': {'name': 'Bird', 'riddle': 'the animal that flies and chirps', 'sound': 'tweet tweet'},
    '🐟': {'name': 'Fish', 'riddle': 'the animal that swims in water', 'sound': 'blub blub'},
    '🐮': {'name': 'Cow', 'riddle': 'the animal that gives us milk', 'sound': 'moo'},
    '🐴': {'name': 'Horse', 'riddle': 'the animal you can ride', 'sound': 'neigh'},
    '🐷': {'name': 'Pig', 'riddle': 'the animal that says oink', 'sound': 'oink oink'},
    '🐸': {'name': 'Frog', 'riddle': 'the animal that jumps and croaks', 'sound': 'ribbit'},
    '🐵': {'name': 'Monkey', 'riddle': 'the animal that swings on trees', 'sound': 'ooh ooh ah ah'},
    '🐻': {'name': 'Bear', 'riddle': 'the big furry animal', 'sound': 'growl'},
}

# Shapes data with riddles
SHAPES_DATA = {
    '🔵': {'name': 'Circle', 'riddle': 'the shape with no corners', 'object': '⚽'},  # ball
    '🔺': {'name': 'Triangle', 'riddle': 'the shape with three sides', 'object': '🍕'},  # pizza slice
    '🟦': {'name': 'Square', 'riddle': 'the shape with four equal sides', 'object': '📦'},  # box
    '🟪': {'name': 'Rectangle', 'riddle': 'the shape like a door', 'object': '🚪'},  # door
    '⭐': {'name': 'Star', 'riddle': 'the shape with five points', 'object': '✨'},  # sparkle
    '❤️': {'name': 'Heart', 'riddle': 'the shape that means love', 'object': '💝'},  # gift heart
    '🔶': {'name': 'Diamond', 'riddle': 'the shape like a kite', 'object': '🪁'},  # kite
}

# Game Modes with level-specific configurations
GAME_MODES = {
    'alphabet': {
        'name': 'Alphabet',
        'description': 'Learn your ABCs!',
        'icon': '🔤',
        'preschool': {
            'target_age': '2.5–3.5 yrs',
            'audio_template': 'Catch the letter {item}',
            'items': list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),  # Uppercase only
            'correct_items': list('AEIOU'),  # Vowels
            'wrong_items': [c for c in 'BCDFGHJKLMNPQRSTVWXYZ'],
            'item_type': 'uppercase',
            'items_on_screen': 3,
            'challenge_focus': 'Visual recognition of capital letters',
        },
        'nursery': {
            'target_age': '3.5–4.5 yrs',
            'audio_template': 'Catch the small letter {item}',
            'items': list('abcdefghijklmnopqrstuvwxyz'),  # Lowercase only
            'correct_items': list('aeiou'),  # Lowercase vowels
            'wrong_items': [c for c in 'bcdfghjklmnpqrstvwxyz'],
            'item_type': 'lowercase',
            'items_on_screen': 5,
            'challenge_focus': 'Matching uppercase to lowercase',
        },
        'kindergarten': {
            'target_age': '4.5–6 yrs',
            'audio_template': 'Catch the letter with sound {phonics}',
            'items': list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            'correct_items': list('BCDFGHJKLMNPQRSTVWXYZ')[:10],  # Consonants
            'wrong_items': list('AEIOU'),  # Vowels are wrong for phonics practice
            'item_type': 'phonics',
            'items_on_screen': 6,
            'challenge_focus': 'Phonics and sound-letter mapping',
            'phonics_map': PHONICS_MAP,
        },
    },
    'animals': {
        'name': 'Animals',
        'description': 'Catch the animals!',
        'icon': '🐾',
        'preschool': {
            'target_age': '2.5–3.5 yrs',
            'audio_template': 'Catch the {name}',
            'items': list(ANIMALS_DATA.keys()),
            'correct_items': ['🐶', '🐱', '🐦', '🐟', '🐮', '🐴'],  # Common/friendly animals
            'wrong_items': ['🦁', '🐘', '🐷', '🐸', '🐵', '🐻'],
            'item_type': 'picture',
            'items_on_screen': 3,
            'challenge_focus': 'Visual recognition of common animals',
            'data': ANIMALS_DATA,
        },
        'nursery': {
            'target_age': '3.5–4.5 yrs',
            'audio_template': 'Catch the word for {name}',
            'items': list(ANIMALS_DATA.keys()),
            'correct_items': ['🐶', '🐱', '🦁', '🐘', '🐦', '🐟'],
            'wrong_items': ['🐮', '🐴', '🐷', '🐸', '🐵', '🐻'],
            'item_type': 'picture+word',
            'items_on_screen': 5,
            'challenge_focus': 'Matching animal picture to its written word',
            'data': ANIMALS_DATA,
        },
        'kindergarten': {
            'target_age': '4.5–6 yrs',
            'audio_template': 'Catch {riddle}',
            'items': list(ANIMALS_DATA.keys()),
            'correct_items': ['🐶', '🐱', '🦁', '🐘', '🐦'],
            'wrong_items': ['🐟', '🐮', '🐴', '🐷', '🐸', '🐵', '🐻'],
            'item_type': 'riddle',
            'items_on_screen': 6,
            'challenge_focus': 'Concept and category recognition',
            'data': ANIMALS_DATA,
        },
    },
    'shapes': {
        'name': 'Shapes',
        'description': 'Identify the shapes!',
        'icon': '⬛',
        'preschool': {
            'target_age': '2.5–3.5 yrs',
            'audio_template': 'Catch the {name}',
            'items': list(SHAPES_DATA.keys()),
            'correct_items': ['🔵', '🔺', '⭐', '❤️'],  # Basic shapes
            'wrong_items': ['🟦', '🟪', '🔶'],
            'item_type': 'picture',
            'items_on_screen': 3,
            'challenge_focus': 'Basic visual shape recognition',
            'data': SHAPES_DATA,
        },
        'nursery': {
            'target_age': '3.5–4.5 yrs',
            'audio_template': 'Catch the word for {name}',
            'items': list(SHAPES_DATA.keys()),
            'correct_items': ['🔵', '🔺', '🟦', '⭐'],
            'wrong_items': ['🟪', '❤️', '🔶'],
            'item_type': 'picture+word',
            'items_on_screen': 5,
            'challenge_focus': 'Matching shape picture to its written word',
            'data': SHAPES_DATA,
        },
        'kindergarten': {
            'target_age': '4.5–6 yrs',
            'audio_template': 'Catch {riddle}',
            'items': list(SHAPES_DATA.keys()),
            'correct_items': ['🔵', '🔺', '🟦', '⭐', '❤️'],
            'wrong_items': ['🟪', '🔶'],
            'item_type': 'riddle',
            'items_on_screen': 6,
            'challenge_focus': 'Shape properties and real-life linkage',
            'data': SHAPES_DATA,
        },
    },
}

# Game Levels - Define difficulty settings
GAME_LEVELS = {
    'preschool': {
        'name': 'Preschool',
        'description': 'Easy and slow',
        'icon': '🌟',
        'base_speed': 1.5,  # Slow
        'spawn_interval': 2000,  # Milliseconds
        'starting_hearts': 5,
        'time_limit': 120,  # 2 minutes in seconds
    },
    'nursery': {
        'name': 'Nursery',
        'description': 'Medium difficulty',
        'icon': '⭐',
        'base_speed': 2.5,  # Medium
        'spawn_interval': 1500,
        'starting_hearts': 4,
        'time_limit': 120,
    },
    'kindergarten': {
        'name': 'Kindergarten',
        'description': 'Fast and challenging',
        'icon': '🎯',
        'base_speed': 3.5,  # Fast
        'spawn_interval': 1000,
        'starting_hearts': 3,
        'time_limit': 120,
    },
}


def get_game_config(mode, level):
    """
    Get the combined configuration for a specific mode and level.
    
    Args:
        mode (str): Mode key (alphabet, animals, shapes)
        level (str): Level key (preschool, nursery, kindergarten)
    
    Returns:
        dict: Combined configuration with mode and level settings
    """
    if mode not in GAME_MODES:
        raise ValueError(f"Invalid mode: {mode}")
    if level not in GAME_LEVELS:
        raise ValueError(f"Invalid level: {level}")
    
    mode_config = GAME_MODES[mode]
    level_specific = mode_config[level]
    
    return {
        'mode': {
            'name': mode_config['name'],
            'icon': mode_config['icon'],
            **level_specific
        },
        'level': GAME_LEVELS[level],
    }
