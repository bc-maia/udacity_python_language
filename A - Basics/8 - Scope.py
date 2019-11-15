# Variable Scope
# Variable scope refers to which parts of a program a variable can
# be referenced, or used, from.

# It's important to consider scope when using variables in functions.
# If a variable is created inside a function, it can only be used
# within that function. Accessing it outside that function is not possible.

# This will result in an error
def some_function():
    word = "hello"  # Local scope


print(word)

# This works fine
def some_function():
    word = "hello"
    # since word is local, it can have different values in different func


def another_function():
    word = "goodbye"


# This works fine, since word is a global scope variable
# Notice that we can still access the value of the global
# variable word within this function. However,
# the value of a global variable can not be modified inside
# the function. If you want to modify that variable's
# value inside this function, it should be passed in as an argument.
word = "hello"


def some_function():
    print(word)


some_function()
