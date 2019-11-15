"""
Try Statement
We can use try statements to handle exceptions. There are four clauses you can use (one more in addition to those shown in the video).

# TODO: try = This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
# TODO: except = If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
# TODO: else = If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
# TODO: finally = Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. 
E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

https://docs.python.org/3/tutorial/errors.html?highlight=exception
"""

while True:
    try:
        x = int(input("\nEnter a number: "))
        break
    except (ValueError, TypeError):
        print("A value different than int input occurs!")
    except KeyboardInterrupt:
        print("\nUser cancelling input")
    finally:
        print("\nInput Attempt.")

# TODO: Accessing Error Messages
# When you handle an exception, you can still access its error message like this:
try:
    pass
    # some code
except ZeroDivisionError as e:
    # some code
    print("ZeroDivisionError occurred: {}".format(e))

# This would print something like this:
# ZeroDivisionError occurred: integer division or modulo by zero

# If you don't have a specific error you're handling, you can still access the message like this:
try:
    pass
    # some code
except Exception as e:
    # some code
    print("Exception occurred: {}".format(e))

