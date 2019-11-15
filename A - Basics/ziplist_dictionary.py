cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}  # TODO: or cast = dict()
for name, height in zip(cast_names, cast_heights):
    cast[name] = height

print(cast)
