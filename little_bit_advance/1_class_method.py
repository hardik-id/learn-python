
# Simple Class with class variable
# Class with init
# Class with StaticMethod
# Class with print method
# Advance class with inheritance


class Person:
    Answer = 42  # Class Variable, Shared by all instance
    def __init__(self, name):
        self.name = name # Instance Variable
        
    @staticmethod
    def something():
        return Person.Answer
        
abc = Person("ABC")
pqr = Person("pqr")

print(abc.name)
print(abc.Answer)
print(pqr.name)
print(pqr.Answer)

abc.Answer = 0
print(abc.Answer)
print(pqr.Answer)

Person.Answer = "How about now?"
print(pqr.Answer)


print(abc.Answer)
del abc.Answer
print(abc.Answer)

print(Person.something())

print("\n\n")

#### Advance Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr((self.name,self.age))
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
    def print_age_class(self):
        print("Child" if self.age < 13 else "Something-else")
        
    @classmethod
    def class_method(cls):
        def new_method(self):
            print(f"New Method {self.name}")
        setattr(cls, 'new_method', new_method)
      
x = Person("ABC",50)  
print(x)
x.print_age_class()
# x.new_method() # This will not work.
x.class_method()
x.new_method() # OR Person.new_method()


###### Inheritance
class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.age_class = "Child"
    def print_category(self):
        print(self.name,self.age,self.age_class)
    def new_method(self):
        print("This will be overridden")

c = Child("Child",2)
c.print_category()
c.new_method()
c.class_method()
c.new_method()



#### Decorator


def uppercase_decorator(function):
    def wrapper():
        result_of_function_execution =  function()
        uppercased = result_of_function_execution.upper()
        return uppercased
    return wrapper

def some_string():
    return "Hello World!"

print(some_string())
decorate = uppercase_decorator(some_string)
print(decorate())

@uppercase_decorator
def some_string_annotation():
    return "Uppercase String!"

print(some_string_annotation())


# Decorator use case:
import requests
@uppercase_decorator
def get_results():
    return requests.get("http://www.mocky.io/v2/5dadc1602d00008040e4bcb3").text

print(get_results())





#### Generator

def number_generator(stop,multiply):
    num = 0
    while(num < stop):
        num += 1
        yield num*multiply
        
print(type(number_generator(5,10)))
print(list(number_generator(5,10)))

print([f"${i}" for i in number_generator(5,10)])

#### Write decorate which converts number list to string with currency symbol
# List: [1, 2, 3, 4]
# Outcome: ['$0', '$1', '$2', '$3', '$4']
