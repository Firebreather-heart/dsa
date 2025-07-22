def fact(x):
    return 1 if x == 1 else x * fact(x-1)
    
def fact2(x):
    if x==1:
        return 1
    else:
        print('x=>', x)
        return x * fact2(x -1)
a = fact2(5)
print(a)