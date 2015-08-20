import sys

class memoize(object):
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value

@memoize
def catalan(n):
    if n <= 1:
        return 1
    else:
        return 2 * (2 * n - 1) * catalan(n-1) / (n + 1)
        
def catalan_partition(n, k):
    total = 0
    for i in range(0, n):
        inside, outside = n - i - 1, i
        part = catalan(inside) * catalan(outside)
        if total < k and total + part >= k:
            return inside, outside, k - total
        else:
            total += part
        
def solve(n, k):
    if k > catalan(n):
        print n, k, catalan(n)
        return "Doesn't Exist!"
    assert k > 0
        
    if n == 1:
        return "()"
    
    array = [""] * (2 * n) #Initialize an empty array of chars we'll fill in with parentheses
    #We always have to open with an open parenthesis
    array[0] = "("
    #Find the number of pairs inside and after the first set, and the lexicographic order of 
    #all these
    inside, after, newk = catalan_partition(n, k)
    #Close the first set
    array[2 * inside + 1] = ")"
    #Figure out the lexicographic count on the sets inside and after the first set
    
    assert newk <= catalan(inside) * catalan(after)
    
    if after:
        k_inside = (newk - 1) // catalan(after) + 1
        k_after = ((newk - 1) % catalan(after)) + 1
    else:
        k_inside = newk
        k_after = 0
    #And recursively fill them in
    if inside:
        array[1:2 * inside + 1] = [char for char in solve(inside, k_inside)]
    if after:
        array[2 * inside + 2:] = [char for char in solve(after, k_after)]
    return ''.join(array)