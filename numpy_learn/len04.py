# python集合示例

animals = {'cat', 'dog'}
print 'cat' in animals
print 'fish' in animals
animals.add('fish')
print 'fish' in animals
print len(animals)
animals.add('cat')
print len(animals)
animals.remove('cat')
print len(animals)

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print nums

# python元组示例
d = {(x, x + 1): x for x in range(10)}
print d
t = (5, 6)
print type(t)
print d[t]
print d[(1, 2)]