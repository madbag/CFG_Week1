# for number in range(9):
#     print('~' * number)
#
# today = input('What day is it? ')
# is_monday = today == 'Monday'
# print('Today is Monday: {}'.format(is_monday))

# temperature = input('What is the temperature? ')
# is_freezing = float(temperature) <= 0.0
# print('The temperature is freezing: {}'.format(is_freezing))

# burger = input('How much is a burger?')
# vegetarian = input('Is the restaurant vegetarian? (y/n)')
#
# cost = float(burger) <= 10.00
# has_vegetarian = vegetarian == 'y'
#
# is_good_choice = cost and has_vegetarian
# if is_good_choice:
#     print('This restaurant is a great choice!')
# if not is_good_choice:
#     print('Probably not a great choice')

# mars_choice = input('Would you like to visit Mars? y/n ')
# is_willing = mars_choice == 'y'
# affordable = input('Can you afford to visit Mars? y/n ')
# can_afford = affordable == 'y'
# should_visit_mars = is_willing and can_afford
# print('You should visit Mars: {}'.format(should_visit_mars))

# password = input('password: ')
# if password == 'jumanji':
#     print('Success!')

# name = input("What is your name? ")
# is_admin = name == 'admin'
#
# password = input("What is your password? ")
# is_password_correct = password == 'dinosaurs'
#
# if is_admin and is_password_correct:
#     print('Welcome')
# else:
#     print('Go away')

# password = input('password: ')
# if password == 'jumanji':
#     print('Success!')
# else:
#     print('Failure!')

# meal_price = float(input('How much did the meal cost? '))
# discount_choice = input('Do you have a discount? y/n ')
#
# is_discount = discount_choice == 'y'
# is_over_twenty = meal_price >= 20.0
# discount_applicable = is_discount and is_over_twenty
#
# if discount_applicable:
#     meal_price = meal_price * 0.9
#     print('Discount Applied!')
# else:
#     print('No discount')
# print('Total cost: {}'.format(meal_price))

# dog_size = int(input('How big is the dog? '))
# if dog_size > 75:
#     print('That is a big dog')
# elif dog_size < 25:
#     print('That is a small dog')
# else:
#     print('That is an average dog')

# temperature = float(input('What is the temperature of the oven? '))
# if temperature > 200:
#     print('The oven is too hot')
# elif temperature < 150:
#     print('The oven is too cold')
# elif temperature == 180:
#     print('The oven is at the perfect temperature')
# else:
#     print('The temperature is close enough')

# import random
# sides = int(input('How many sides does the die have? '))
# random_integer = random.randint(1, sides)
# print('You rolled a {}'.format(random_integer))

# import random
# def flip_coin():
#     random_number = random.randint(1, 2)
#     if random_number == 1:
#         side = 'heads'
#     else:
#         side = 'tails'
#     return side
# choice = input('heads or tails: ')
# result = flip_coin()
# print('The coin landed on {}'.format(result))

import random
def random_choice():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice

my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))
if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')