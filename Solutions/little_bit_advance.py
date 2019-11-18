#### Excersice convert number list to string with currency symbol
# List: [1, 2, 3, 4]
# Outcome: ['$0', '$1', '$2', '$3', '$4']

def curreny_decorator(func):
    def wrapper():
        return [f"${i}" for i in func]
    return wrapper

y = curreny_decorator(range(5))
print(y())



# # Exercise 1:
# Create Multiply method to multiply all the arguments passed as positional arguments.


#     input: multiplyAll([1,2,3])
#     Output: 6

#     input: multiplyAll([1,2,3,0])
#     Output: 0

# First Aproach
def multiplyAllFor(*args):
    result = 1
    for x in args: result = result * x
    print(result)
    
multiplyAllFor(1,2,3)
multiplyAllFor(1,2,3,0)

# Second Aproach
from functools import reduce

def multiplyAll(*args):
    print(reduce(lambda a,b: a*b,args))
    
multiplyAll(1,2,3)
multiplyAll(1,2,3,0)


