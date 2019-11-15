import other_script

print("hello")

# TODO: Using a main block
# To avoid running executable statements in a script when it's imported as a module in another script,
# include these lines in an if __name__ == "__main__" block. Or alternatively,
# include them in a function called main() and call this in the if main block.

print(
    other_script.main()
)  # this main method only runs when invoked, in opposite of __main__ dunder
