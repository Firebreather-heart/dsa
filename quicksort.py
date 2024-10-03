def quicksort(arr:list):
    # print(arr)
    if len(arr) < 2:
        # print(arr)
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        print(f'{left} <=> [{pivot}] <=> {right}')
        return quicksort(left) + [pivot] + quicksort(right)
    
arr = [3,1,2,4,5,8,7,6,9,10]
print(quicksort(arr))