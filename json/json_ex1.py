import json

data = {
    "user": {
        "name": "John Doe",
        "age": 30,
    }
}

with open("json/data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

json_str = json.dumps(data, indent=4)
print(json_str)