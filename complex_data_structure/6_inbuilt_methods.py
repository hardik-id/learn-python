####### MAX MIN LEN SUM

print(max([1,2,3,4]))
print(min([1,2,3,4]))
print(len([1,2,3,4]))
print(sum([1,2,3,4]))



####### All ANY
print(all([True,True,True]))
print(all([True,False,True]))
print(all([1,2,3]))
print(all([1,2,0]))
print(all([1,2,0]))
print([True if str(x).startswith("H") else False for x in "Hello World".split(" ")])
print(all([True if str(x).startswith("H") else False for x in "Hello World".split(" ")]))
print(any([True if str(x).startswith("H") else False for x in "Hello World".split(" ")]))


####### SORT method

x= sorted([2,3,1])
print(x)

x = sorted({1: 'D', 2: 'B', 3: 'B', 5: 'A', 4: 'E'})
print(x)

x = sorted("This is a test string from Andrew".split(), key=str.lower)
print(x)

x=sorted([("a",10),("b",15),("c",5)],key=lambda i: i[1])
print(x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr((self.name,self.age))
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
    
x = sorted([Person("ABC",50),Person("PQR",20)], key=lambda p: p.age)
print(x)

print(Person("ABC",10)==Person("ABC",20))

####### range method
print(range(10))
for i in range(3): print(i)
print(list(range(10)))
print(list(range(5,10)))
print(list(range(0,10,3)))
print(list(range(10)[::3]))
print(list(range(10)[::-1]))



####### enumerate method
print("\n### Loop Over List")
for i, item in enumerate(["ABC", "PQR", "XYZ"]):
    print(i, item)
    
####### zip method
list_x = ["ABC","XYZ","PQR"]
list_y = [20,21]
for x,y in zip(list_x, list_y):
    print(f'{x} is {y} years old.')


####### iter method
itr = iter(["Hello","World","!"])
print(next(itr),next(itr), next(itr))
itr = iter(["Hello","World","!"])
for word in itr:
    print(word)

#### https://realpython.com/python-data-types/



##### Random
from random import shuffle
x = list(range(10))
shuffle(x);
print(x)

from random import randint
print(randint(0,100))
print(randint(0,100))