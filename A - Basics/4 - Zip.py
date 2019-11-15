# Zip and Enumerate
# zip and enumerate are useful built-in functions that can come
# in handy when dealing with loops.

# Zip
# zip returns an iterator that combines multiple iterables into one
# sequence of tuples. Each tuple contains the elements in that position
# from all the iterables. For example, printing

a = list(zip(["a", "b", "c"], [1, 2, 3]))
print(a)
# would output [('a', 1), ('b', 2), ('c', 3)]


# TODO: 1 - You could unpack each tuple in a for loop like this.
letters = ["a", "b", "c"]
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# TODO: 2 - Or You could unpack/unzip using asterisk
some_list = [("a", 1), ("b", 2), ("c", 3)]
letters, nums = zip(*some_list)
print(letters, nums)

# Enumerate
# enumerate is a built in function that returns an iterator of tuples
# containing indices and values of a list. You'll often use this
# when you want the index along with each element of an iterable in a loop.
letters = ["a", "b", "c", "d", "e"]

for i, letter in zip(range(len(letters)), letters):
    print(i, letter)

# same as above can be done using enumerate:

for i, letter in enumerate(letters):
    print(i, letter)
