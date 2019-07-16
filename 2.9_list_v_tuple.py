# Lists vs Tuples

'''
    Definition of Constant folding:
    the process of recognizing and evaluating constant expressions at compile time
    rather than computing them at runtime
'''

from dis import dis

(1, 2, 3)
[1, 2, 3]

dis(compile('(1, 2, 3, "a")', 'string', 'eval'))
print('-------------------------------------')
dis(compile('[1, 2, 3, "a"]', 'string', 'eval'))
print('-------------------------------------')

from timeit import timeit

# We can run timeit() on a tuple and a list. Lists are immutable, but process slower

print(timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=10_000_000))
print('-------------------------------------')
print(timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=10_000_000))

def fun1():
    pass


dis(compile('(fun1, 10, 20)', 'string', 'eval'))

'''
A tuple (t1) making another tuple has the same memory address. 
thus t2 = tuple(t1)
id(t1) == id(t2) 
because tuples are immutable, it doesn't make sense to have a different address
'''

t = tuple()
prev = sys.getsizeof(t)
for i in range(10):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c)')


l = list()
prev = sys.getsizeof(t)
for i in range(10):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c)')

c = list()
prev = sys.getsizzeof(l)
print(f'0 items: {prev}')
for i in range(255):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta={delta}')

t = tuple(range(100_000))
l = list(t)

timeit('t[99_999]', globals=globals(), number=10_000_000)
timeit('l[99_999]', globals=globals(), number=10_000_000)

