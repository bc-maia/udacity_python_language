# Please use this space to test and run your code
num_list = [
    422,
    136,
    524,
    85,
    96,
    719,
    85,
    92,
    10,
    17,
    312,
    542,
    87,
    23,
    86,
    191,
    116,
    35,
    173,
    45,
    149,
    59,
    84,
    69,
    113,
    166,
]

odd_sum, odd_count = 0, 0
odd_list = []

while odd_count <= 5:
    if num_list[odd_count] % 2 != 0:
        odd_list.append(num_list[odd_count])
    odd_count += 1

# print(odd_list)
print(sum(odd_list))
