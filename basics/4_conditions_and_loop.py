################ IF
x = True
if x:
    print("True")
################ IF ELSE IF
x = "test"
if x == 1:
    print("Value of x is 1.")
elif x == "test":
    print("Value of x is test.")
################ NESTED IF ELSE
if 1 == 2:
    print("1==2")
    if 2 == 1:
        print("1==2")
    elif 2 == 2:
        print("2==2")
else:
    if 1 == 1:
        print("Nested: 1==1")

################ In line condition
print("Okay") if 1 == 1 else False

################ AND OR < Operators
if True and False:
    print("True and False")
if True and True:
    print("True and True")
if True or False:
    print("True or False")

print(1-1 or "Something")
print(10+1 or "Something")
print([1, 2] < [1, 2, 5])

################ LOOP - WHILE
x = 5
while (x >= 0):
    print(x)
    x = x - 1;

print("Out of loop\n")

################ LOOP - WHILE ELSE
x = 5
while (x >= 0):
    print(x)
    x = x - 1;
else:
    print("Value of x is now: ",x)

print("Out of loop\n")


################ LOOP - WHILE - IN LINE
x = True
while(x): print("Definetly True"); x = False;
print("Out of loop\n")

################ LOOP - FOR
print("\n### Loop Over List")
for item in ["ABC", "PQR", "XYZ"]:
    print(item)
print("\n### String")
for item in "Universe":
    print(item)
print("\n### Loop over range")
for i in range(5):
    print(i)
else:
    print("Else of for executed.\n")
    

################ LOOP - CONTINUE and BREAK
for i in range(5):
    if(i==2):
        continue
    print(i)
print("Out of loop\n")
for i in range(5):
    if(i==2):
        break
    print(i)
print("Out of loop\n")
