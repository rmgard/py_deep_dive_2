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


dis(compile('(fn1, 10, 20)', 'string', 'eval'))
