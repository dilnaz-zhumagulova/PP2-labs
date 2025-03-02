file = open('dir_files/text.txt', 'r')

cnt = 0
for _ in file:
    cnt+=1

print(cnt)