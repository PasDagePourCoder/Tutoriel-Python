### Variables ###

# This is a comment

age = 15

age = 13

age_limit = 18

difference_age: int = age - age_limit

division_age: float = age / age_limit

name: str = 'Naruto'

sentence = 'Naruto a ' + str(age) + ' ans'

# Incrementation

age = 15

age = age + 3
age += 3

name = name + ' Uzumaki'
name += ' Uzumaki'

a, b = 5, 8


# Interaction avec la console

print('Hello')
print('Age: ', age)

age_user = input('Quel est ton age?')

difference_age = int(age_user) - 18
print('Age is', difference_age)


### Boolean Type ###

is_minor: bool = True
age = 14
is_minor: bool = (age < 18)

### Naming Conventions ###

differenceAge = 15

difference_age_ninja = 15
is_minor

weather_temperature_degrees_celsius = 15
weather_temperature_fahrenheit = 70


# Exercices #

# 1. Demander age et nom et afficher dans le chat #

age_user = input('Quel est ton age?')
name_user = input('Quel est ton nom?')

print('Le nom est ', name_user, ' et age est: ', age_user)


# 2. Trouver des noms pour les variables suivantes: le prix de l'essence, l'anniversaire de la Reine
# d'angleterre et le createur de Mona Lisa

price_oil_euros: float = 1.55
anniversary_queen_of_england: str = '01/01/2000'
mona_lisa_creator: str = 'Da Vinci'

# 3. Echanger la valeur de deux variables de trois facons différentes:
# - En une ligne
# - En utilisant une autre variable
# - Sans usage d'autres variables

a = 5
b = 8

a, b = 8, 5

# 2

c = a
a = b
b = c

# 3

a = a + b
b = a - b
a = a - b
