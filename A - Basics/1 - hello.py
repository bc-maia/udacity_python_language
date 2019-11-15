print("hello")

a, b, c = 1, 2.4, 3
print(type(a))
print(int(b))
print(float(c))

x, y, z = 0.1, 0.1, 0.1
print(x + y + z)  # odd result 0.30000000000000004

text = "this is a string"
print(type(text))
print(f"{len(text)} characters long")
print(text[8])

str_value = "12312312"
print(float(str_value))

new_str = "The cow jumped over the moon."
print(new_str)
print(new_str.split())  # Splits all

print(new_str.split(sep=" ", maxsplit=3))  # Splits using separator

print(new_str.count("o"))

print(new_str.rfind("o"))

