import sys

spell = sys.stdin.readline().strip()

chars = {}
for char in spell:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1
        
maxcount = max(chars.values())
for key in chars:
    if chars[key] == maxcount:
        print key
        break