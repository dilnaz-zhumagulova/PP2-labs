def returning(n):
    for i in range(n+1, -1, -1):
        yield i

ret = returning(9)
for i in range(11):
    print(next(ret))