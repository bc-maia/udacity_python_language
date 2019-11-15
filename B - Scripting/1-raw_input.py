# get and process input for a list of names
names = input("\nPlease, enter students names:\n").split(",")
names = [name.strip() for name in names]

# get and process input for a list of the number of assignments
assignments = input("\nPlease, inform the assignments left per student:\n").split(",")
assignments = [float(assign.strip()) for assign in assignments]

# get and process input for a list of grades
grades = input("\nEnter the current grades by student:\n").split(",")
grades = [float(gr.strip()) for gr in grades]

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
data = zip(names, assignments, grades)

for name, assign, grade in data:
    new_score = grade + assign * 2
    print(message.format(name, assign, grade, new_score))


# sample input
# john doe, john wick, john john
# 5, 2, 7
# 70, 90, 50
