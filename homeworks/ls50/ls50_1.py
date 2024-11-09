import yaml

with open("config.yaml", "r") as fl:
    config = yaml.safe_load(fl)

config["server"]["port"] = 9090

with open("config.yaml", "w") as fl:
    yaml.safe_dump(config, fl)

