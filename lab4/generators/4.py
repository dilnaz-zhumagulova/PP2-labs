def squares_inrange(a, b):
    for i in range(a, b+1):
        yield (i*i)

squares = squares_inrange(2, 10)
for i in range(2, 11):
    print(next(squares))