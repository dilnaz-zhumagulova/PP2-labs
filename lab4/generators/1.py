def generator(n):
    for i in range(1, n+1):
        yield i**2

makeSquares = generator(5)
for i in range(5):
    print(next(makeSquares))
