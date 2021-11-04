### 4 Les Dictionnaires ###
from typing import List, Dict, Tuple, Any

ninja = {}

ninja: Dict[str, Any] = {
    'name': 'Naruto',
    'age': 15,
    'level': 3,
    'is_minor': True
}

'level' in ninja

ninja['village'] = 'Konoha'
ninja['age'] = 17

print(ninja)

ninja.values()

### Example avec des listes ###

ninjas_list = [('Naruto', 18, 3)]

ninjas_dict: List[Dict[str, Any]] = [
    {'name': 'Naruto', 'age': 15},
    {'name': 'Sasuke', 'age': 17},
]

ninjas_dict[0]['name']

ninjas_dict_variation: Dict[str, Dict[str, Any]] = {
    'Naruto': {'age': 15, 'level': 3, 'meals': ['ramen', 'tofu', 'sushi']},
    'Sasuke': {'age': 17, 'level': 5}
}

user_name = 'Naruto'

ninjas_dict_variation['Naruto']['meals']

ninja_name = input('Quel ninja veux-tu connaitre? ' + str(ninjas_dict_variation.keys()))
print('Son age est: ', ninjas_dict_variation[ninja_name]['age'], 'son level est: ',
      ninjas_dict_variation[ninja_name]['level'])

### Exercices ###

# 1. Mergez les deux dictionnaires suivants:

ninja = {'name': 'Naruto', 'age': 15}
hero = {'name': 'Sasuke', 'popularity': 5}

z = {**hero, **ninja}


# 2. Créer une structure qui permet aisément en fonction d'une ville, et d'une personne de trouver sa notation
# Et de trouver facilement les villes visitées par cette personne

# Villes: Paris, London
# Personnes: Alice, Bob, Charlie


notation_cities = {
    'Paris': {'Alice': 5, 'Bob': 3, 'Charlie': 4},
    'London': {'Alice': 1},
}

notation_cities['London']['Bob']

users = {
    'Alice': {'cities_visited': ['Paris', 'London']},
    'Bob': {'cities_visited': ['Paris']},
}