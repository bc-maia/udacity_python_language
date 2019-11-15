# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# TODO: Iterate through the dictionary
for key, value in basket_items.items():
    if key in fruits:
        # TODO: if the key is in the list of fruits,
        # add the value (number of fruits) to result
        result += value

print(result)


# TODO: Creating function and running with multiple lists / dictionaries
def item_checker(basket, fruits):
    result = 0
    for fruit, value in basket_items.items():
        if fruit in fruits:
            # TODO: if the key is in the list of fruits,
            # add the value (number of fruits) to result
            result += value
    return result


# Example 1
result = 0
basket_items = {'pears': 5, 'grapes': 19,
                'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
result = item_checker(basket_items, fruits)
print(result)


# Example 2
result = 0
basket_items = {'peaches': 5, 'lettuce': 2,
                'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
result = item_checker(basket_items, fruits)
print(result)


# Example 3
result = 0
basket_items = {'lettuce': 2, 'kites': 3,
                'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
result = item_checker(basket_items, fruits)
print(result)

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for item, count in basket_items.items():
    # if the key is in the list of fruits, add to fruit_count.
    if item in fruits:
        fruit_count += count
    # if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += count

print(fruit_count, not_fruit_count)
