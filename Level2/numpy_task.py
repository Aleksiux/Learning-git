import random

import numpy as np

from_zero_to_hero = np.arange(1, 10)
zeros = np.zeros(10)
ones = np.ones(10)
fours = np.ones(10) * 4
even_numbers = np.arange(0, 101, 2)
matrix = np.arange(1, 26).reshape(5, 5)

print(matrix)
print('-' * 100)
print(matrix[2, 1])
# print(matrix[2:3, 1:2]) # other way.
print(matrix[-1])
print('-' * 100)
print(matrix[:3, :3])
print('-' * 100)
print(matrix[1:4, 1:])
print('-' * 100)
print(matrix[3:, :3])
print('-' * 100)

rand_flo = np.random.sample(20)
print(rand_flo)
print('-' * 100)
print(rand_flo.max())
print(rand_flo.argmax())
print('-' * 100)
print(rand_flo.min())
print(rand_flo.argmin())
print('-' * 100)
print(rand_flo.dtype)
print('-' * 100)

rand_int_number = np.arange(1, 101)
bool_rand = rand_int_number > 90
print(rand_int_number[bool_rand])
print('-' * 100)
# rand_int_number = [num for num in rand_int_number if num % 7 == 0]
print(rand_int_number[rand_int_number % 7 == 0])
print('-' * 100)
matrix_of_fl = np.linspace(0.025, 1, 40)
reshaped_array = matrix_of_fl.reshape(5, 8)
print(reshaped_array)
print('-' * 100)
matrix_from_two_to_tousand = np.arange(2, 1001)
matrix_sqrt = [num for num in matrix_from_two_to_tousand if np.sqrt(num) % 1 == 0]
matrix_reshape = np.array(matrix_sqrt).reshape(6, 5)
print(matrix_reshape)
print('-' * 100)
new_var = np.arange(1, 101)


def check_for_primary(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


new_func = np.vectorize(check_for_primary)
bool_primary = new_func(new_var)
print(new_var[bool_primary])
