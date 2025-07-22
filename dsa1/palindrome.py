def chckpal(word):
    word = [i for i in word]
    return (word == word[::-1])

print(chckpal("radar"))