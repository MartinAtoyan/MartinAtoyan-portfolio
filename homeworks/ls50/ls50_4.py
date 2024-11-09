import json

with open("user_data.json", "r") as data_json:
    data = json.load(data_json)

filtered_data = []

for i in data:
    if i.get("age") > 30 and i.get("role") == "manager":
        filtered_data.append(i)

with open("filtered_data.json", "w") as fl:
    json.dump(filtered_data, fl, indent=1)

