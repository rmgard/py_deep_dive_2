l = [1, 2, 3]
t = (1, 2, 3)
s = 'python'

""" the above are all sequence types which are indexable and iterable.
We can reference elements inside the sequence by their indeces
l[0] = 1
t[1] = 2
s[2] = 't'
"""

""" We can also loop or iterate over them:
    """

for c in s: 
    print (c)

####################################################################
# Sets are also iterable
# They are not sequence types, so they don't support indexing
# something such as set1[1] would return an error

set1 = {10, 20, 30}

for e in set1: 
    print(e)

set2 = {'x', 10, 'a', 'A'}

for e in set2:
    print(e)
