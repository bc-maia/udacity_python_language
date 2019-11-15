# https://docs.python.org/3/howto/functional.html?highlight=iterables#iterators
"""
Iterators And Generators
Iterables are objects that can return one of their elements at a time, such as a list.
Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.

An iterator is an object that represents a stream of data. This is different from a list,
which is also an iterable, but is not an iterator because it is not a stream of data.

Generators are a simple way to create iterators using functions. 
You can also define iterators using classes, which you can read more about here.

Here is an example of a generator function called my_range, 
which produces an iterator that is a stream of numbers from 0 to (x - 1).
"""

# the function is a generator
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1


# the iterastor is the result of calling this function

"""
# https://docs.python.org/3/howto/functional.html?highlight=iterables#generators

https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235
Generators are a lazy way to build iterables. They are useful when the fully realized 
list would not fit in memory, or when the cost to calculate each list element is high 
and you want to do it as late as possible. But they can only be iterated over once.
"""


# TODO: QUIZ Example with standard function and generator function
# Standard function
lessons = [
    "Why Python Programming",
    "Data Types and Operators",
    "Control Flow",
    "Functions",
    "Scripting",
]

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# generator function
def my_enumerate(iterable, start=0):
    # Implement your generator function here
    for it in iterable:
        yield (start, it)
        start += 1


# printing the iterable
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# TODO: QUIZ Chunker
# Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i : i + size]  # iterable[5:9] in chuncks of 4


for chunk in chunker(range(25), 4):
    print(list(chunk))


# TODO: Generator Expressions
# Here's a cool concept that combines generators and list comprehensions!
# You can actually create a generator in the same way you'd normally write a list comprehension,
# except with parentheses instead of square brackets. For example:

sq_list = [x ** 2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x ** 2 for x in range(10))  # this produces an iterator of squares
# This can help you save time and create efficient code!
