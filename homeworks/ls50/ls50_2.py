import json
import yaml

with open("data.yaml", "r") as yaml_fl:
    data = yaml.safe_load(yaml_fl)

with open("data.json", "w") as json_fl:
    json.dump(data, json_fl, indent = None)

