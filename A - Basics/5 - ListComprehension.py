#!/home/maia/.pyenv/versions/3.7.4/bin/python3
# -*- coding: utf-8 -*-

# TODO: Examples Not using list comprehension
# List comprehensions allow us to create a list using a for loop in one step.

# TODO: Sample 01 - capitalized city names
cities = ["atlanta", "new york", "mountain view", "springfield", "portland"]
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
# print(capitalized_cities)

# TODO: Sample 02 - list of squares
squares = []
for x in range(9):
    squares.append(x ** 2)
# print(squares)


# TODO: Samples using list comprehension
# TODO: sample 01 - capitalized city names
list_comprehension_capt_cities = [city.title() for city in cities]
print(list_comprehension_capt_cities)

# TODO: Sample 02 - list of squares
list_comprehension_squares = [x ** 2 for x in range(9)]
print(list_comprehension_squares)

# TODO: Sample 03 - update names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

user_names = [name.replace(" ", "_").lower() for name in names]
first_names = [name.split(" ")[0].lower() for name in names]

print(tuple(zip(first_names, user_names)))

# TODO: Sample 04 - 20 first multiples of 3
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

# TODO: Sample 05 - filtering dict by value
scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98,
}

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
