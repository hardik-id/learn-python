# Multi line string
x = """This is test string which 
can span across 
multiple lines """

print(x)

# Search in string
x = "Do parallel universe exist?"
print(x, "PARALLEL universe" not in x)
print(x, "PARALLEL universe".lower() in x)
print("universe in '"+x+"' is at index:", x.find("universe"))

# String is array [start,end,step]
print("Print String Twice: ", x*2)
print("x[12]: ", x[12])           # Print Character at index 12 "u"
print("x[12:20]: ", x[12:20])     # Print string between index 12 to 20 "universe"
print("x[12:]: ", x[12:])         # Print string starting at index 12 to the end. "universe exists?"
print(x[-6:])                     # Print string started at index 6 backward  "exist?"
print(x[::2])                     # Print every send character of string
print(x[::-1])                    # Reverse String


# print("Answer to life the universe and everything is " + 42) This will not work
print("Answer to life the universe and everything is {}.".format(42))
print("Answer to {1} the universe and everything is {0}.".format(42, "life"))
print("Answer to {answer} the universe and everything is {thing}.".format_map({"answer":42,"thing":"life"}))
# Event better way of formatting string
answer = 42
thing = "life"
print(f"Answer to {answer} the universe and everything is {thing}.")

# Store raw string
print('Hello\nWorld!')
print(r'Hello\nWorld!')



# Methods of String


print("hello world!".capitalize())
print("Hello World!".isalpha())
print("   Hello World!   ".strip())
print(",".join(["Hello","World!"]))
print("Hello World!".startswith("H"))

#Reference: https://docs.python.org/3.8/library/stdtypes.html#string-methods


x = input("What is your name? ")
print("Hello " + str(x))