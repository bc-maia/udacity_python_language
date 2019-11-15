from pprint import pprint


# LISTS are orderable, mutable sequence of items
list_of_random_things = [1, 3.4, "a string", True]
list_of_random_things.append("new stuff")
print(list_of_random_things)

list_of_random_things[-1]  # returns the last item of the list


slicing = [1, 2, 3, 4, 5, 6]
# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
slicing[1:3]  # => [2, 4]
# Omit the beginning and return the list
slicing[2:]  # => [4, 3]
# Omit the end and return the list
slicing[:3]  # => [1, 2, 4]
# Select every second entry
slicing[::2]  # =>[1, 4]
# Return a reversed copy of the list
slicing[::-1]  # => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
## slicing[start:stop:step]


print("a" not in slicing)  # false
print(3 in slicing)  # true


# ALERT: Slice is an object that normalizes the slice by the sequence length
slicing = [1, 2, 3, 4, 5, 6]
slicer = slice(1, 2, 2)
print(slicing[slicer])

# TODO: the syntax notation is a SYNTAX SUGAR for:
print(slicing.__getitem__(slice(len(slicing), 0, -1)))

# syntax sugar:
print(slicing[::-1])


state = "the quick brown fox jumps over the lazy dog"
print(sorted(set(state)))  # TODO: Strings can be sorted using sorted function

# TODO: BuiltIn functions https://docs.python.org/3/library/functions.html
# Useful Functions for Lists I
# returns how many elements are in a list.
len(slicing)

# returns the greatest element of the list. How the greatest
# element is determined depends on what type objects are in the list.
# The maximum element in a list of numbers is the largest number.
# The maximum elements in a list of strings is element that would
# occur last if the list were sorted alphabetically.
# This works because the the max function is defined in terms of
# the greater than comparison operator. The max function is undefined
# for lists that contain elements from different, incomparable types.
max(slicing)

# returns the smallest element in a list. min is the opposite of max,
# which returns the largest element in a list.
min(slicing)

# returns a copy of a list in order from smallest to largest,
# leaving the list unchanged.
sorted(slicing)

# Joining list items as string
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

print(len(names))


# Tuples - They are often used to store related pieces of information.
# Related pieces of information Immutable ordered sequence of elements
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

pprint(location)
pprint(dimensions)


# Sets
# data type for mutable unordered collections of unique elements.
# One application of a set is to quickly remove duplicates from a list.
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()  # Removest the first element.


# Dictionary
# dictionary is a mutable data type that stores mappings of
# unique keys to values.
# Here's a dictionary that stores elements and their atomic numbers.
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements["helium"])  # print the value mapped to "helium"
# insert "lithium" with a value of 3 into the dictionary
elements["lithium"] = 3

print("carbon" in elements)
print(elements.get("dilithium"))
# .get() returns None if the key isn't found. elements["dilithium"]
# does returns error instead

# Define a Dictionary, population, that provides information on the
# world's largest cities.
# The key is the name of a city (a string), and the associated value
# is its population in # millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}
print(population)


# Solution: Count Unique Words
verse = "if you can keep your head when all about you are losing theirs and\
blaming it on you if you can trust yourself when all men doubt you\
but make allowance for their doubting too if you can wait and not\
be tired by waiting or being lied about  don’t deal in lies or\
being hated don’t give way to hating and yet don’t look too good\
nor talk too wise"
print(verse, "\n")

# split verse into list of words
verse_list = verse.split()
print(verse_list, "\n")

# convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, "\n")

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)


# Solution: Verse Dictionary
verse_dict = {
    "if": 3,
    "you": 6,
    "can": 3,
    "keep": 1,
    "your": 1,
    "head": 1,
    "when": 2,
    "all": 2,
    "about": 2,
    "are": 1,
    "losing": 1,
    "theirs": 1,
    "and": 3,
    "blaming": 1,
    "it": 1,
    "on": 1,
    "trust": 1,
    "yourself": 1,
    "men": 1,
    "doubt": 1,
    "but": 1,
    "make": 1,
    "allowance": 1,
    "for": 1,
    "their": 1,
    "doubting": 1,
    "too": 3,
    "wait": 1,
    "not": 1,
    "be": 1,
    "tired": 1,
    "by": 1,
    "waiting": 1,
    "or": 2,
    "being": 2,
    "lied": 1,
    "don't": 3,
    "deal": 1,
    "in": 1,
    "lies": 1,
    "hated": 1,
    "give": 1,
    "way": 1,
    "to": 1,
    "hating": 1,
    "yet": 1,
    "look": 1,
    "good": 1,
    "nor": 1,
    "talk": 1,
    "wise": 1,
}
print(verse_dict, "\n")

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])
