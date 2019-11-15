"""
TODO: The Python Standard Library has a lot of modules! To help you get familiar with what's available, 
here are a selection of our favourite Python Standard Library modules and why we use them!

csv: very convenient for reading and writing csv files
collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
string: more functions on strings. This module also contains useful collections of letters like string.digits 
    (a string containing all characters which are valid digits).
re: pattern-matching in strings via regular expressions
math: some standard mathematical functions
os: interacting with operating systems
os.path: submodule of os for manipulating path names
sys: work directly with the Python interpreter
json: good for reading and writing json files (good for web work)
We hope you find these useful!
"""


import math

print(math.pow(math.e, 3))
print(math.exp(3))

import random

# Use an import statement at the top

word_file = "words.txt"
word_list = []

# fill up the word_list
with open(word_file, "r") as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    # return (word_list.pop() + word_list.pop() + word_list.pop())  or
    # return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)  or
    return "".join(random.sample(word_list, 3))


# test your function
print(generate_password())


import timeit

print(timeit.Timer())

