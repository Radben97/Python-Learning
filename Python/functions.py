def hello():
    print("hello world")

hello()

def sum(a=0,b=0):
    
    if(type(a) is not int or type(b) is not int):
        return
    print(a + b)

sum(1,2)


""" def negate(a):
    return not a

bloop = negate(True)
print(bloop) """

# multiple arguments

def multiple_items(*args): # multiple arguments are passed as tuples
    print(args)
    print(type(args))

multiple_items(1,2,3,4,5)

# multiple args with unknown arguments

def mult_named_args(**kwargs): # multiple named arguments are pased as dicts
    print(kwargs)
    print(type(kwargs))

mult_named_args(name="dave", age = 30, city="new york")