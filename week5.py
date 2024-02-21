# zoo = [
# {'species': 'zebra', 'name': 'Penelope'},
# {'species': 'penguin', 'name': 'Jenn'},
# {'species': 'elephant', 'name': 'Harris'},
# {'species': 'flamingo', 'name': 'Florence'},
# ]
#
# for animal in zoo:
#     print(animal['species'])

# with open('people.txt', 'w+') as text_file:
#     people = 'Joanne \nSusan \nAmina'
#     text_file.write(people)

# with open('people.txt', 'r') as text_file:
#     contents = text_file.read()
#     print(contents)

# new_item = input('Enter a to-do item')
#
# with open('todo.txt', 'r') as todo_file:
#     todo = todo_file.read()
#
# todo = todo + new_item + '\n'
#
# with open('todo.txt', 'w+') as todo_file:
#     todo_file.write(todo)

# import csv
# #
# # field_names = [ 'name', 'age']
# #
# # data = [
# #     {'name': 'Jill', 'age': 32},
# #     {'name': 'Sara', 'age': 28},
# # ]
# #
# # with open('team.csv', 'w+') as csv_file:
# #     spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
# #     spreadsheet.writeheader()
# #     spreadsheet.writerows(data)
# #
# import csv
# # # with open('team.csv', 'r') as csv_file:
# # #     spreadsheet = csv.DictReader(csv_file)
# # #     for row in spreadsheet:
# # #         print(dict(row))
#
# with open('trees.csv', 'r') as csv_file:
#     spreadsheet = csv.DictReader(csv_file)
#
#     heights = []
#
#     for row in spreadsheet:
#         tree_height = row['height']
#         heights.append(tree_height)
#
# shortest_height = min(heights)
# print(shortest_height)

import requests
pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()

print("Pokemon: ", pokemon["name"])

moves = pokemon['moves']
for move in moves:
    print(move['move']['name'])
