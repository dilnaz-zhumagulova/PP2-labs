def num(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield i
        
divisible = num(100)
for i in range(9):
    print(next(divisible))