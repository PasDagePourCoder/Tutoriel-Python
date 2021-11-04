### 5 - Les Conditions ###

faim: bool = False
is_breakfast: bool = True
soif: bool = False

if faim:
    # Si c'est vrai
    print('Je mange')
    if is_breakfast:
        print('un petit dejeuner')
    else:
        print('Un autre repas')
elif soif:
    print('Je bois')
else:
    # Si c'est faux
    print('je dors')


### Conditions plus complexes ###

heure = 20
condition = 'soif'
heure >= 20

# Test Egalite

condition == 'soif'

if heure >= 18 and condition == 'faim':
    print('je mange')
else:
    print('je ne mange pas')


### De Morgan Law ###

# NOT( C1 OR C2) <=>  NOT C1 AND NOT C2

if not heure >= 18 or not condition == 'faim':
    print('je ne mange pas')
else:
    print('je mange')


if heure < 18 or condition != 'faim':
    print('je ne mange pas')
else:
    print('je mange')


###

name = 'Sasuke'
list_hero = ['Naruto', 'Sasuke']

'toto' in list_hero

### Conditions Imbriquees ###

is_ninja: bool = True
age = 22
name ='Naruto'

if is_ninja:
    if age >= 18:
        # He is major
        if name in list_hero:
            print('Hero!')
        else:
            print('Adult ninja')
    else:
        print('Ninja Child')
else:
    print('This is not a ninja')


### Exercices ###

# 1. Implémenter une calculatrice, prenant en entrée deux nombres, une opération et renvoyant le résultat

number_1 = int(input('Premier nombre: '))
number_2 = int(input('Second nombre: '))
operation: str = input('Operation? (addition, multiplication, soustraction, division')

if operation == 'addition':
    result = number_1 + number_2
elif operation == 'soustraction':
    result = number_1 - number_2
## Idem with multiplication and division
else:
    print('Operation is not known')
print('The result is', result)

# 2. Si (je suis un mammifère et que mon age est supérieur à 20) ou (que je ne suis pas un mammifère
# et que mon age est supérieur à 10) alors je suis une espèce menacée

is_mammal = False
animal_age = 15

if (is_mammal and animal_age >= 20) or (not is_mammal and animal_age >= 10):
    print('Endangered Species')
else:
    print('It is okay')

