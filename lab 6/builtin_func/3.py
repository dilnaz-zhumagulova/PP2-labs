s = input()
s = s.replace(' ', '') 
if s == s[::-1]:
    print("Yes")
else:
    print("No")