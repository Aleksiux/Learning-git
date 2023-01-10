from time import sleep
import time
from functools import wraps


def limit_func_para(function):
    def wrapper(*args):
        result = function(args)
        if len(args) > 2:
            print(f'Maximum arguments is 2 allowed.')
            return ""
        elif len(args) <= 1:
            print(f"You need to add 2 arguments for function")
            return ""
        return result

    return wrapper


def program_time_it(func):
    @wraps(func)
    def timeit_wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Program took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


def return_string(func):
    def wrapper(text):
        result = func(text)
        if type(result) != str:
            print("Only string inputs are allowed.")
            return ""
        else:
            return result

    return wrapper


def wait(stime):
    def wait(fn):
        def wrapper(*args):
            sleep(stime)
            print(f"Functions sleep time was {stime} secs.")
            return fn(*args)

        return wrapper

    return wait


@return_string
def return_str(text):
    return text


@wait(3)
@limit_func_para
# @return_string
def sum_all(*args):
    return sum(*args)


@program_time_it
def looping(x):
    for x in range(x):
        result = x * 100
    return result


print(sum_all(5, 20))
# print(return_str("Testas"))
# print(looping(1000000))
