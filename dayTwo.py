# Session 2 - WEEK 2
# User Input
# age = input('What is your age?')
# print('Hello, I am {} years old'.format(age))

# Exercise 2.1:
# fruit = input('What fruit do you like? ')
# veg = input('What veg do you like? ')
# print('You like {} and you like {}'.format(fruit, veg))

# apples_string = '12' || apples_string = str(12)
# total_apples = int(apples_string) + 5
# print(total_apples)
# output from the input function will always be string

# purchased_apples = input('How many apples did you buy? ')
# print(type(purchased_apples))
# total_apples = int(purchased_apples) + 5
# print(total_apples)
# type(total_apples)

# Exercise 2.2:
# friends = input('How many friends? ')
# pizzas = (int(friends)+1) * 2
# print('You need {} pizzas for {} friends'.format(pizzas, friends))

# Python Modules
# re for big data - or search

# For Loops
# student = ("anna", "john", "maria")
#
# for myStudent in student:
#     print("Hello {}".format(myStudent))

# Zero indexing
# for number in range(1,11):
#     print(number+10)

# for character in 'Banana':
#     print(character)

# for name in ['Mary', 'Ranjit', 'Fatima']:
#     print(name)

# for number in range(5):
#     print("executing FOR LOOP - run No {}".format(number + 1))

# total = 0
# print("*** This statement is OUTSIDE THE LOOP")
# print("Before the loop executes, our TOTAL is equal to = ", total, '\n')
# print("--------------------------------------------------------")
# for number in range(3): # remember --> 0, 1, 2
#      print("This is loop execution for digit: " + str(number) + " inside the loop \n")
#      print("Updating total... (+ 1) \n")
# total = total + 1 # every time the loop executes, we add 1 to th
# print("--------------------------------------------------------")
# print("***This statement We is OUTSIDE the loop now")

# While Loop
# store_capacity = 10
# while store_capacity > 0:
#     print('Please come in. Spaces available: ' + str(store_capacity))
#     store_capacity = store_capacity - 1
# print("\nPlease wait for someone to exit the store.")

# Functions
# Create a function
# def hello():
#     print('Hello, class!')
#
# hello()

# Pass Argument
# def hello(name):
#     print('Hello,', name)
#
# hello('Maria')
# hello('Kim')
# hello('Olya')

# def some_function(name, job):
#     print(name, 'is a', job)
# some_function('Fiona', 'Developer')

# Function Arguments
# Wrong order
# def some_function(name, job):
#     print(name, 'is a', job)
# some_function('developer', 'Fiona')

# Keyword Arguments
# def some_function(name, job):
#     print(name, 'is a', job)
# some_function(job='developer', name='Fiona')
# some_function(name='Fiona', job='developer')

# Default Argument
# def some_function(name, job='developer'):
#     print(name, 'is a', job)
# some_function('Fiona')
# some_function('Fiona', 'manager')

# Returning Values from Function
# Using return statement
# def sum(x, y):
#     return x + y
# result = sum(10, 15)
# print("result is: {}".format(result))

# Without return statement
# def sum(x, y):
#     print(x + y)
# result = sum(10, 15)
# print("result is: {}".format(result))

# Without return statement
# def sum(x, y):
#     return x + y
# result = sum(10, 15)
# print("result is: {}".format(result))

# Exercise 2.6:
# def circle_area():
# # add the radius argument inside the brackets
# area = 3.14 * (radius ** 2)
# # add return statement
# circle_1 = circle_area(10)
# print(circle_1)

# Solved
# def circle_area(radius):
#     # add the radius argument inside the brackets
#     area = 3.14 * (radius ** 2)
#     return area
#
# area = circle_area(10)
# print(area)

# def days_in_hours(days):
#     hours = days * 24
#     return hours
#
# print(days_in_hours(10))

# Combine FOR loop and FUNCTION
# def times_two(num):
#     result = num * 2
#     return result
#
# for number in range(3): # 0,1,2
#    calc_res = times_two(number)
#    print(calc_res)

import datetime
# x = datetime.datetime.now()
# print(x)

my_date = datetime.date(2020, 12, 31)
print(my_date.strftime("%d-%b-%Y"))


