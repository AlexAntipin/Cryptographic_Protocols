# from itertools import combinations
# from numpy import sum as npsum
#
# def combs(matr):
#     arr = []
#     for k in range(2, len(matr) + 1):
#         rows = combinations(matr,k)
#         indices = list(combinations(range(len(matr)), k))
#         for i, j in enumerate(rows):
#             if sum(npsum(j, axis=0) % 2) == 0:
#                 arr.append(indices[i])
#     return arr
# #[[14, 1, 1, 13], [13, 15, 11, 16], [16, 6, 7, 6], [15, 12, 10, 11]]
# #[[2, 2, 16, 8], [15, 6, 7, 7], [11, 14, 12, 10], [2, 2, 2, 14]]
# print(combs([[14, 1, 3, 8], [2, 1, 9, 0], [3, 9, 11, 9], [5, 16, 1, 6]]))

str_to_conv = "Let's learn Python"
# printing the string that will be converted
print("The string that we have taken is ",str_to_conv)
# using join() + ord() + format() to convert into binary
bin_result = ''.join(format(ord(x), '08b') for x in str_to_conv)
print("The string that we obtain binary conversion is ",bin_result)
bin_result = int(bin_result, 2)
print(bin_result.to_bytes((bin_result.bit_length() + 7) // 8, 'big').decode())

bin_result = int(bin_result, 2)
print(bin_result)


