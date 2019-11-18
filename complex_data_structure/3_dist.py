### DICTIONARY
print("\n\n### DICTIONARY")
dict_json = {"Name":"ABC", "Age": 20}
print(dict_json)
print(dict_json["Name"])
print(dict_json.get("Name"))
dict_json["Age"] = 22
print(dict_json)
del dict_json["Age"]
print(dict_json)


# Functions
dict_json = {"Name":"ABC", "Age": 20}
print(dict_json == {"Name":"ABC", "Age": 20}) #  Comparison
print(len(dict_json))  # Length of key-value pair

# Important Methods
print(list(dict_json))   # List of keys
tupple_to_dict = dict([
    ("tuple_colume1","tuple_colume2"), 
    ("tuple_colume1","tuple_colume2")
    ])
print(tupple_to_dict)

print({x : x*2 for x in (1,2,3)})


data = {
    "Name": "ABC",
    "Age": 20
    }
for key,value in data.items():
    print(f'{key}: {value}')
    
print(data.items())
print(data.keys())
print(data.values())
print("Name" in dict_json)
data.update({"Age":23})
print(data)
    
    
    
    
    
### JSON
print("\n\n##### JSON")

import json

x = '{"name":"ABC","age":20}'

y  = json.loads(x)
print(type(x).__name__)
print(type(y).__name__)
print(y['name'])

# The Otherway around.
z = json.dumps(y)
print(type(z))
print(z)


x = {"foo": ["bar", "baz"]}
z =json.dumps(x)
print(type(x))
print(type(json.JSONEncoder().encode({"foo": ["bar", "baz"]})))