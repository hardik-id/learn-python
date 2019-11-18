f = open("./data.txt", "r")

data = f.read()
print(data)
print(f.closed)
f.close()

print("\n\n## with option")
# File close automatically
with open("data.txt","r") as f:
    read_line = f.read()
    print(read_line)
    
print(f.closed)




print("\n\n## Readline")
# Readline, memory efficient

with open("data.txt", "r") as f:
    for line in f.readlines():
        print(repr(line))
        print("Loop end")
        

    
with open("data.txt", "r") as f:
    for line in f:
        print(line, end=' ')
        
        
print("\n\n## JSON")
# Dump json to file
f = open("output.json", "w+")
import json
x = { "key1": "value1", "key2":[1,"Two"]}
print(json.dumps(x))

json.dump(x,f)


print("\n\n### Read JSON file")
### Read JSON file
f = open('output.json')
print(json.load(f))

# Modes available to open file https://www.tutorialspoint.com/python/python_files_io.htm