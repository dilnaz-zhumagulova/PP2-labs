import time

number = int(input())
milliseconds = int(input())
time.sleep(milliseconds/1000)
square = number ** 0.5
print('Square root of', number, 'after', milliseconds, 'is', square)