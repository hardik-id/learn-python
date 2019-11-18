
#  EXERCISE 1:
# Step 1: Join items from list `["Answer","to","life","the","universe","and","everything","is","42"]` with space.
# Step 2: Append it with . at the end of line.
print(" ".join(["Answer","to","life","the","universe","and","everything","is","42"])+'.')

#  EXERCISE 2:
#Find how many occurances of "a" in the "Answer to life the universe and everything is 42."
print("Answer to life the universe and everything is 42.".casefold().count("a"))

#  EXERCISE 3:
#Print last 3 digits of "Answer to life the universe and everything is 42."
print("Answer to life the universe and everything is 42."[-3:])

# EXERCISE 4:
# Delete element from list.
print("\nExercise 1:")
x = [1,"test",3]
print(x)
del x[1]
print(x)


# EXERCISE 5:
# Practice insert, append, remove, reverse
print("\nExercise 2:")
x = [1,2]
x.append(["append",4])
print(x)

x = [1,2]
x.insert(1,["insert",4])
print(x)

x = [1,2]
x.remove(1)
print(x)

x = [1,2]
x.reverse()
print(x)

x = [2,1,3,5,4]
x.sort()
print(x)


x = [1,2,3,4,5]
poped = x.pop(1)
print(x)
print(poped)