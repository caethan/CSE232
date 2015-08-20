import sys

amusing = sys.stdin.readline().strip()
newword = sys.stdin.readline().strip()

prefixes = set()
for i in range(len(amusing)):
    prefixes.add(amusing[:i+1])

#print prefixes

cache = {}

def is_splittable(S):
    if S in cache:
        return cache[S]
    
    if S in prefixes:
        cache[S] = S
        return S
    
    count = min(len(S), len(amusing))
    #print count
    for j in range(count)[::-1]:
        idx = len(S) - j - 1
        suffix = S[idx:]
        #print idx, suffix
        if suffix in prefixes:
            if is_splittable(S[:idx]):
                val = '%s %s' % (is_splittable(S[:idx]), suffix)
                cache[S] = val
                return val
            else:
                cache[S] = ''
                return ''
    
    cache[S] = ''
    return ''
        



"""splittable = ['' for char in newword]

for i in range(len(newword))[::-1]:
    substr = newword[i:]
    if substr in prefixes:
        splittable[i] = substr
    else:
        for j in range(min(len(substr), len(amusing))):
            if substr[:j+1] in prefixes:
                if splittable[i + j + 1]:
                    splittable[i] = '%s %s' % (substr[:j+1], splittable[i + j + 1])
                    continue
if splittable[i]:
    print 'No\n%s' % splittable[i]
else:
    print 'Yes'"""
    
if is_splittable(newword):
    print 'No\n%s' % is_splittable(newword)
else:
    print 'Yes'