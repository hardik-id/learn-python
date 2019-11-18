#  EXERCISE 1:
# Practice: Ask for name and age both and print them together.
# Console Output: `John is 30 years old.`name = input('What is your name? ')
name = input('What is your name? ')
age = input('What is your age? ')
print(f'{name} is {age} years old.')



#  EXERCISE 2:
# do same execersice with for loop without using string join method.

# - Step 1: Create py file and run.
# - Step 2: Join items from list ["Answer","to","life","the","universe","and","everything","is","42"] with space.
# - Step 3: Append it with . at the end of line.

x = ["Answer","to","life","the","universe","and","everything","is","42"]
result = ""
for word in x:
    result = result + word + " "
print(result[:-1]+".")


# Alternate approach
x = ["Answer","to","life","the","universe","and","everything","is","42"]
result = ""
i = 1
for word in x:
    result = result  + word + (" " if i != len(x) else "")
    i += 1
    
print(result+".")
