import re

s = input('Input your string: ')

def insert_spaces(s):
    spaced_text = re.sub(r'(?<!^)([A-Z])', r' \1', s)
    return spaced_text

print(insert_spaces(s)) 