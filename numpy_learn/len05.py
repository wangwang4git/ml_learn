# python函数示例

def sgin(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print sgin(x)

def hello(name, loud = False):
    if loud:
        print 'Hello, %s' % name.upper()
    else:
        print 'Hello, %s!' % name

hello('Bob')
hello('Fred', loud = True)

# python类示例

class Greeter(object):
    
    def __init__(self, name):
        self.name = name

    def greet(self, loud = False):
        if loud:
            print 'Hello, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name

g = Greeter('Fred')
g.greet()
g.greet(loud = True)