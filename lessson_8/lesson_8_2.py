# N = 5

# result =  []
# for num in range(1, N + 1):
#     result.append(num ** 2)

# result = [num ** 2 for num in range(1, N + 1)]
# print(result)


# numbers = [1234, 2443, 33, 54, 5545, 654, 745, 854, 9]
# result_numbers = [num > 35 for num in numbers]
#
# print(result_numbers)


numbers = [1234, 2443, 33, 54, 5545, 654, 745, 854, 9]
result_numbers = [num for num in numbers if num > 35 or num == 0]
# result = []
# for num in numbers:
#     if num > 35:
#         result_numbers.append(num ** 2)
# print(result_numbers)

# numbers = [-1123, -2543, -333, -545, -5545, 654, 745, 854, 9]
# result= []
# for num in numbers:
#     if num >= 0:
#         result.append(f"{num} - положительное")
#     else:
#         result.append(f"{num} - отрицательное")
#
# print(result)

# result = [f"{num} - положительное" if num >= 0 else f"{num} - отрицательное" for num in numbers]
# print(result)

# table_multiply = [
#     f"{x} * {y} = {x * y}"
#     for x in range(1, 10)
#     for y in range(1, 10)
# ]

# table_multiply = []
# for x in range(1, 10):
#     for y in range(1, 10):
#         table_multiply.append(f"{x} * {y} = {x * y}")
#
# print(table_multiply)