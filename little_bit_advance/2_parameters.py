# Positional parameter
def sumAll(a,b):
    print(a+b)

sumAll(1,2)
# keyworded parameter
sumAll(b=1,a=2)


def sumAll(a,b=0):
    print(a+b)
# Default parameter
sumAll(1)


# *args
def sumAll(*args):
    print(args)
    print(sum(args))
    
    
sumAll(1,2,3)



# **kwargs
def printName(**kwargs):
    print(f"Name is {kwargs['name']}" if 'name' in kwargs else "NoName Argument")

printName(age=12)
printName(name="Bond, James Bond")

def printNameAge(**kwargs):
    if(set(['name','age']) <= set(kwargs)):
         print(f"Name: {kwargs['name']}, Age: {kwargs['age']}")


printNameAge(name="ABC", anotherKey=234)
printNameAge(name="ABC", age= 20, anotherKey=234)


# args and kwargs both together
def argsKwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    
    
argsKwargs(12,"test",myKey1="value",myKey22=12)
# argsKwargs(12,"test",myKey1="value",myKey22=12, 123) This will not work.


print("abcde"[::-2])