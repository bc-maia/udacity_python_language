# initiate empty list to hold user input and sum value of zero
user_list = []  # sample input: 23, 24, 25, 26, 27, 28, 29, 30, 31, 22
list_sum = 0

# seek user input for ten numbers
for i in range(10):
    userInput = int(input("\nEnter any 2-digit number: "))

    # check to see if number is even and if yes, add to list_sum
    # print incorrect value warning  when ValueError exception occurs
    try:
        user_list.append(userInput)
        if userInput % 2 == 0:
            list_sum += userInput
    except ValueError:
        print("\nIncorrect value. That's not an int!\n")
    except KeyboardInterrupt:
        break

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))
