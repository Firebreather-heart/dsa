import time 
from functools import wraps 

def runtime(func):
    @wraps(func)
    def wrapper(arr: list, item):
        start = time.time()
        res = func(arr, item)
        end = time.time()
        print(f'program run in {end-start} seconds')
        return res
    return wrapper
