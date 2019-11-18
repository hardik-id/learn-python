x = 1
print("Type: "+type(x).__name__)

x = 1.3
print("Type: "+type(x).__name__)

x = "abc"
print("Type: "+type(x).__name__)

x = {1, "test", "ABC"}
print("Type: "+type(x).__name__)

x = {"key": "value"}
print("Type: "+type(x).__name__)

x = (1, "test", 2, 3)
print("Type: "+type(x).__name__)

x = [1, "test", 2, 3]
print("Type: "+type(x).__name__)


x = range(3)
print("Type: "+type(x).__name__)

x = True
print("Type: "+type(x).__name__)

x = set(["A", "B"])
print(hasattr(x, "__iter__"))
print(dir(x))

# Method details at https://docs.python.org/3/library/index.html
# Advance Data Types: https://docs.python.org/3/library/datatypes.html

