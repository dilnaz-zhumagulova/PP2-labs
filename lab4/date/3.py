import datetime
x = datetime.datetime.now()
m = x.replace(microsecond=0)
print(m)