
def print_unique(arr:list):
    """Big O: O(n^2)"""
    if not isinstance(arr, list):
        raise ValueError("arr must be a list.")
    else:
        arr = list(set(arr))
        cnt = 1
        for i in arr:
            for j in arr[cnt:]:
                print(i, j)
            cnt += 1

