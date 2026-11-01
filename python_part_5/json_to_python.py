import json

json_data = '{"name" : "Reduan", "age" : 54}'

# converted to python dictionary
dic = json.loads(json_data)

print(dic)