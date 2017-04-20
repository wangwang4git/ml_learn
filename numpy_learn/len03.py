# python字典示例

d = {'cat': 'cute', 'dag': 'furry'}
print d['cat']
print 'cat' in d
d['fish'] = 'wet'
print d['fish']
# print d['monkey']
print d.get('monkey', 'N/A')
print d.get('fish', 'N/A')

del d['fish']
print d.get('fish', 'N/A')

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)

for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x : x ** 2 for x in nums if x % 2 ==0}
print even_num_to_square