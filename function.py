#n, k = map(int, input().split())
#print(n + k)

#x = input().split()
#xs = (int(i) for i in x)

'''
def even(x):
    return x % 2 == 0

evens = filter(even, xs)
for i in evens:
    print(i)
'''

#even = lambda x : x % 2 == 0

#evens = list(filter(even, xs))
#print(evens)
'''
x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

def length(name):
    return len(" ".join(name))

name_lengths = [length(name) for name in x]
print(name_lengths)

x.sort(key = length)
print(x)

x.sort(key = lambda name : len(" ".join(name)))
print(x)
'''

'''
import operator as op

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4))

x = [1 ,2, 3]
f = op.itemgetter(1)
print(f(x))

x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

x.sort(key = op.itemgetter(-1))
print(x)


from functools import partial

x = int("1101", base = 2)
print(x)

int_2 = partial(int, base = 2)
x = int_2("1101")
print(x)


x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

import operator as op
from functools import partial

sort_by_last = partial(list.sort, key = op.itemgetter(-1))
print(x)
sort_by_last(x),
print(x)
'''

def mod_checker(x, mod=0):
    return lambda y: y % x == mod

mod_3 = mod_checker(3)
print(mod_3(3))
print(mod_3(4))

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4))