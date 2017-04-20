xs = [3, 1, 2]
print xs, xs[2]
print xs[-1]
xs[2] = 'foo'
print xs
xs.append('bar')
print xs
x = xs.pop()
print x, xs

nums = range(5)
print nums
print nums[2 : 4]
print nums[2 : ]
print nums[ : 2]
print nums[ : ]
print nums[ : -1]
nums[2 : 4] = [8, 9]
print nums

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print animal

for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares

squares = [x ** 2 for x in nums]
print squares

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares