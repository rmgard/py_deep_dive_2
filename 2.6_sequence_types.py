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

""" A list is mutable, so we can reassign elements. Thus,
l[0] = 100
------> l == [100, 2, 3] is true
tuples are immutable, so we could not say:
t[0] = 100
In other words, the memory address of the object can't be changed.
We can alter things with a mutable object within them...
"""

t2 = ([1, 2], 3,4 )

"""
t[0] = [1, 2, 3] will not work.
But, this will work:"""

t2[0][0] = 100

""" most sequence types handle the 'in' and 'not in' operators
"""

'a' in ['a', 'b', 100] # True

100 in range(200) # True

