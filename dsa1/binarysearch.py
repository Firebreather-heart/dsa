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


# @runtime
def binsearch(arr: list, item):
    print(arr)
    low = 0
    n = len(arr) - 1
    mid = (low + n)//2
    if arr[mid] == item:
        return mid
    else:
        if arr[mid] > item:
            return binsearch(arr[:mid], item)
        elif arr[mid] < item:
            res = binsearch(arr[mid+1:], item)
            return mid + 1 + res

start = time.time()
print('(binarysearch 001): element found at index: ',
      binsearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
end = time.time()
print(f"program run in {end-start} seconds")


@runtime
def binsrch(arr: list, item):
    def _binsrch(arr: list, item, low, high):
        print(arr)
        mid = (high + low) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return _binsrch(arr, item, low, mid - 1)
        else:
            return _binsrch(arr, item, mid + 1, high)
    return _binsrch(arr, item, 0, len(arr) - 1)


print('(binarysearch 002): element found at index: ',
      binsrch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
