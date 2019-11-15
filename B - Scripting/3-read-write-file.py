# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# TODO: Read file
f = open("test_file_read.txt", "r")
file_data = f.read()
f.close()

print(file_data)

# TODO: Write to file
f = open("test_file_write.txt", "w")
f.write("potatoes")
f.close()

# With
# TODO: Python provides a special syntax that auto-closes a file for you once you're finished using it.
with open("test_file_read.txt", "r") as f:
    file_data = f.read()

# If you pass the read method an integer argument, it will read up to that number of characters,
# output all of them, and keep the 'window' at that position ready to read on.
with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

# Reading line by line
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
