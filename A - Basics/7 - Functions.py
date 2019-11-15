# Defining Functions
# Example of a function definition:
def cylinder_volume_function(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


# After defining the cylinder_volume function, we can call the function like this.
cylinder_volume_function(10, 3)


# Return or Not?
# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)


# this returns something
def add_ten(num):
    return num + 10


print("Calling show_plus_ten...")
return_value_1 = show_plus_ten(5)
print("Done calling")
print("This function returned: {}".format(return_value_1))

print("\nCalling add_ten...")
return_value_2 = add_ten(5)
print("Done calling")
print("This function returned: {}".format(return_value_2))


# Default Arguments
# We can add default arguments in a function to have default values
# for parameters that are unspecified in a function call.


def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name
