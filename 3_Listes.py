### Listes ###
from typing import List, Tuple

price_oil = 1.55

prices_oil_list = [1.55, 1.9, 1.8]

len(prices_oil_list)

prices_oil_list.append(1.6)

prices_oil_list.remove(1.8)

### Index ###

prices_oil_list.pop(1)

prices_oil_list.sort()

prices_oil_list.reverse()

names = ['Naruto', 'Sakura', 'Sasuke']
names[0]

prices_oil_list: List[float] = [1.55, 1.9, 2]


### Tuples ###

names_tuple = ('Naurto', 18)
names_tuple + (1)

### Listes de Listes ###

prices_oil_june = [5, 3, 4]
prices_oil_april = [5, 8, 7]

prices_oil_year: List[List[int]] = [
    prices_oil_june,
    prices_oil_april,
    [1, 5, 7]
]

prices_oil_year[1][-1]

### Exercices ###

# 1. Construire une liste de liste de tuples et
# # acceder a l'avant dernier de chaque

ninja_info_per_cohort: List[List[Tuple[str, int]]] = [
    [('Naruto', 18), ('Sakura', 13)],
    [('Neiji', 20), ('Rock Lee', 17)]
]

sentence = 'The name of the last of last cohort is: ' + ninja_info_per_cohort[-1][1][0]