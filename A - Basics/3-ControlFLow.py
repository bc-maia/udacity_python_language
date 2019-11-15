# IF STATEMENT
phone_balance = 199
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

# If, Elif, Else
season = "summer"
if season == "spring":
    print("plant the garden!")
elif season == "summer":
    print("water the garden!")
elif season == "fall":
    print("harvest the garden!")
elif season == "winter":
    print("stay indoors!")
else:
    print("unrecognized season")

points = 1
if points < 51:
    prize = "wooden rabbit"
elif points > 50 and points < 151:
    prize = "no prize"
elif points > 150 and points < 181:
    prize = "wafer-thin mint"
elif points > 180 and points < 201:
    prize = "penguin"

points = 174  # use this input to make your submission

# write your if statement here
win_quote = "Congratulations! You won a {}!"
if points < 51:
    result = win_quote.format("wooden rabbit")
elif points > 50 and points < 151:
    result = win_quote.format("no prize")
elif points > 150 and points < 181:
    result = win_quote.format("wafer-thin mint")
elif points > 180 and points < 201:
    result = win_quote.format("penguin")
else:
    prize = "Oh dear, no prize this time."
#
# OR
#
if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)


# Complex Boolean Expressions examples
# For really complicated conditions you might need to combine some ands,
# ors and nots together. Use parentheses if you need to make the combinations
# clear.

# if 18.5 <= weight / height**2 < 25:
#     print("BMI is considered 'normal'")

# if is_raining and is_sunny:
#     print("Is there a rainbow?")

# if (not unsubscribed) and (location == "USA" or location == "CAN"):
#     print("send email")


#
##
###
# FOR
###
cities = ["new york city", "mountain view", "chicago", "los angeles"]
for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities)

# Range function
limit = 100
range(start=0, stop=limit, step=1)
print(range(4))
print(range(2, 6))
print(range(1, 20, 3))


#
##
###
# WHILE
###
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) < 17:
    hand.append(card_deck.pop())

print(hand)


# Factorial using loops

# WHILE LOOP #########
# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

# FOR LOOP #########
# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)
