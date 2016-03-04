import functools

#1:makebold(makeitalic(hello))
def makebold(fn):
    def wrapped():
        return "<b>"+fn()+"</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>"+fn()+"</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()
 
#2:log(now)
def log(func):
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
	
@log
def now():
    print '2015-3-25'

now()

#3:log('execute')(now)
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator
	
@log('execute')
def now():
    print '2015-3-25'
	
now()


#4:#2
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return wrapper
	
#5:#3
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator