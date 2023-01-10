# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         current_value = self.start
#         self.start += 1
#         return current_value
#
#
# nums = MyRange(1, 10)
# import time
# import itertools
#
# start_time = time.time()
#
# list_of_cubes = [x ** 3 for x in range(1_000_000)]
# delta_time = time.time() - start_time
# print(f'List of cubes created in {delta_time:.2f} seconds')
#
# start_time = time.time()
# cube_generator = (x ** 3 for x in range(1_000_000))
# delta_time = time.time() - start_time
# print(f'Generator of cubes took {delta_time:.2f} seconds')
#
# print(list_of_cubes[:15])
# print(list(itertools.islice(cube_generator, 15)))
# 1 task

# def multi():
#     count = 2
#     while True:
#         yield count
#         count += 2

#
# counter = multi()
# print(next(counter))
# 2 task
# def fibonacci():
#     a = 0
#     b = 1
#     while True:
#         c = a + b
#         yield c
#         a = b
#         b = c
#
#
# fib = fibonacci()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# 3task

# def check_pin(pin):
#     for i in range(10000):
#         check = '{0:04}'.format(i)
#         if check == pin:
#             yield check
#             print(f'{check} == {pin} you cracked the code :)')
#             break
#
#
# checking = check_pin('1425')
# for x in checking:
#     try:
#         print(next(checking))
#     except StopIteration:
#         break


def return_file_print(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        while True:
            result = f.readline()
            yield result


file = return_file_print("task1_regex")
print(next(file))
print(next(file))
print(next(file))
