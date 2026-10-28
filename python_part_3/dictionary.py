dict = {
    "name" : "Reduan",
    "age" : 34,
    "University" : "UIU"
}

"""
Dictionary Keys must be unique
Dictionary Keys must be immutable (e.g., strings, numbers, tuples)
Dictionary is mutable.
Dictionary values can be anything (lists, other dictionaries, etc.)
Unordered (although in modern Python, dictionaries preserve insertion order)

"""

print(dict.keys())
print(dict.values())
print(dict.items())


print(dict.get("name"))
new_item = {"location" : "Dhaka"}
dict.update(new_item)
print(dict)
