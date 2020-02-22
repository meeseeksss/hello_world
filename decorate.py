def decorate(func):
    def wrapper():
        print('decorating')
        func()
        print('decorated')
    return wrapper
@decorate
def tree():
    print('a')

tree()
def tree():
    print('b')
    
def space():
  count=0
  for i in range(5):
    count+=1
    if count==3:
        print('-----------------')
    else:
        print('\n')
space()
tree=decorate(tree)
tree()
print('\nsame')
space()
print('now with arguments')
def adecorate(*args,**kwds):
    print('outer decorator gets decorate arguments')
    print('start real decoration after receiving arguments')
    print('arguments:',args)
    def decorate(func):
        print('received function and start decorating')
        def wrapper(*args,**kwds):
            print('decorating',end=':')
            print(func.__name__,end=',')
            print('function arguments:',args)
            func(*args,**kwds)
            print('decorated')
        print('wrapper gets function arguments\n')
        return wrapper
        print('return wrapper')
    print('real decorator gets function\n')
    return decorate
    print('return decorate')
@adecorate(1,2,4)
def undecorated(*args,**kwds):
    print('not decorated')
undecorated(2,3,7)
print('\nthings wont be executed after return')
print('because only the returned will be executed')

print('''\n\nouter decorator returns true decorator,who will then
return the wrapper, which includes the original function''')
space()
print('multiple decorator')
def cdecorate(a,b):
    def decorate(func):
        print('duh')
        def wrapper():
            print(a+'decorating')
            func()
            print(b+'decorated')
        return wrapper
    return decorate
@cdecorate('1','3')
@cdecorate('2','4')
def justsomerandomfunction():
    print('wow')
justsomerandomfunction()
print('first from far to near, then near to far')
