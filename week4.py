# List and dictionaries

# carrots = input('How many carrots do you have? ')
# rabbits = 6
# if rabbits < carrots:
#     print('There are not enough carrots')
# if rabbits > carrots:
#     print('There are too many carrots')
# else:
#     print('You have the right number of carrots')

# Lists

# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
# print(student_names[2])
# # Helena

# Exercise 4.1
# clothes = [
# "shorts",
# "shoes",
# "t-shirt",
# ]
# if clothes[0] == 'shorts':
#     clothes[0] = 'warm coat'
#
#     print(clothes)

# List functions
# costs = [1.2, 4.3, 2.0, 0.5]
# print(len(costs))
# print(max(costs))
# print(min(costs))

# costs = [1.2, 4.3, 2.0, 0.5]
# print(sorted(costs))
# print(list(reversed(costs)))

# # Exercise 4.2
# list = [ 3, 10, 52, 22, 63, 200, 156, 46, 98, 20]
# print(len(list))
# print(max(list))
# print(min(list))

# Append () and in
# student_name = input('Which student are you looking for? ')
# students = [
# 'Diedre', 'Hank', 'Helena', 'Salome',
# ]
# if student_name in students:
#     print('{} is in the class'.format(student_name))
# else:
#     print('{} is not in the class'.format(student_name))

# students = [
# 'Diedre', 'Hank', 'Helena', 'Salome',
# ]
# student_name = input('What is the name of the new student? ')
# students.append(student_name)
# print(students)

# Exercise 4.3
# shop_list = ["bread", "cheese", "Onion"]
# # list_add = input('Do you want to add something?')
# if 'bread' in shop_list:
#     shop_list.append('butter')
# print(shop_list)

# fridge = [
# 'cheese',
# 'pizza',
# 'coke',
# ]
# if 'milk' not in fridge:
#     print('You have no milk in the fridge')

# For loop and lists
# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
# for student_name in student_names:
#     print(student_name)

# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
# count = 0
# for student_name in student_names:
#     count = count + 1
# print(count)

# Exercise 4.4
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
# for cost in costs:
#     total_cost = total_cost + cost
# print(total_cost)
# total = sum(costs)
# print(total)

# Dictionaries
# person = {
# 'name': 'Jessica',
# 'age': 23,
# 'height': 172
# }
#
# print(person['name'])
# print(person['age'])

# place = {
# 'name': 'The Anchor',
# 'post_code': 'E14 6HY',
# 'street_number': '54',
# 'location': {
# 'longitude': 127,
# 'latitude': 63,
# }
# }
#
# print(place['name'])
# print(place['post_code'])
# print(place['street_number'])
# print(place['location']['longitude'])
# print(place['location']['latitude'])

# Dictionaries in Lists
# people = [
# {'name': 'Jessica', 'age': 23},
# {'name': 'Trisha', 'age': 24},
# ]
# for person in people:
#     print(person['name'])
#     print(person['age'])

# Exercise: 4.6
# fruits = [
# {'name': 'apple', 'colour': 'red', 'price': 0.12},
# {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
# {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# for fruit in fruits:
#     print(fruit['name'])
#     print(fruit["colour"])
#     print(fruit["price"])

import random
# colours = ['red', 'green', 'blue']
# chosen_colour = random.choice(colours)
# print(chosen_colour)

# Exercise 4.7
list_first = ['jake', 'tony', 'nate', 'alice', 'berty']
list_last = ['scott', 'halpert', 'paul', 'rando', 'beesly']

chosen_name = random.choice(list_first) + " " + random.choice(list_last)

print(chosen_name)