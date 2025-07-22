"""This program checks if an element exists in a list"""

def find(arr: list, x:int|str|object):
    "Big O : 0(n)"
    if not isinstance(arr, list):
        raise TypeError("First argument must be a list")
    for i in arr:
        if i == x:
            return True
    return False
