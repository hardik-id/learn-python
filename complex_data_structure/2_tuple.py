### TUPLE
print("\n\n### TUPLE")
x = (1,2,"Three",4)
print(x)
x = 1,2,"Three",4
print(x)

# Index
x = (1,2,"Three",4)
print(x[1])
print(x[1:-1])

# Mutate Tuple?
x = (1,2)
print(x*4)
y = ("Three",4)
print(x+y)
print(x+y)
print(1 in x)
for i in x: print(i)

# Following will not work
# del x[1] 
# y[1] = 3 