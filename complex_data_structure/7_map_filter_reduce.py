######## map
# Transform each object of list
# i.e. multiple each object by 3 in [0,1,2,3]
x = range(5)
print(list(x))
y = map(lambda x: x*3,x)

def multiply_5(num):
    return num*5

print(list(y))
y = map(multiply_5,x)
print(list(y))

######## filter
# Removed items from list based on condition
y = filter(lambda i: i%2==0, x)
print(list(y))


######## reduce
from functools import reduce
y = reduce(lambda a,b: a+b, x)
print(y)


####### Play around with OS module.
import os
import time


print(time.time())
print(os.getcwd())
print(os.listdir())

x = ["ABC","ABCD","PQR"]
x_lower = list(map(str.lower, x))
print(x_lower)
print([w for w in x if w.startswith('A')])

x = [2,4,6,8,10]
x_2 = list(map(lambda i: i/2, x))
print(x_2)


value = list(map(lambda x: str(x).startswith('p'), os.listdir()))

print(value)


print(list(filter(lambda x: str(x).find("cwd") > 0, dir(os))))

print([x for x in dir(os) if x.find("cwd") > 0])




######## del keyword
x= [1,2,3]
print(x)
del x[1]
print(x)

x = {"key1":"Value1","key2":"Value2"}
print(x)
del x['key1']
print(x)





######## in keyword
print("a" in ["a","b"])
print("a" in "abc")
x = {"a":1}
print("a" in x)
x = {"key":"a"}
print("a" in x.values())
