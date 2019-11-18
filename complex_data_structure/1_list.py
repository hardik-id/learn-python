### LIST
x = [1,2]
print(x)

x = list(("tuple",1))
print(x)

x = [i for i in range(5)]
print(x)

x = [
        1,
        "ABC",
        ["Another","List"],
        ("tuple","as","well"),
        {"Dictionary":True}
    ]
print(x)


# Common method os list.
print(dir([]))

x = "Answer to life the universe and everything is 42."
print(x.casefold().count("a"))

# Compare two array
print(["a"]==["a"])

# Extend Array
print([1,2]+["Three",4])
x = [1,2]
x.extend(["Three",4])
print(x)

# Repeat values
print([1,2]*3)

# Slice and Index
x = ["a","b","c","d"]
print(x[1:3])
print(x[1])


# Try this yourself and tell us what is the outcome.
# x = 'Hello World!'
# print(x[1:-1])

# Mutate element on List
x = ["a","b","c","d"]
x[1] = 0
print(x)

# Importance of copy
x = [1,2,3,4]
y = x # x.copy() or list(x)
y[1] = "Changed"
print(x)

# List comprehension


x = []