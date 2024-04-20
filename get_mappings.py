import re, os, json, yaml

mapping_path: str = os.path.expandvars("%appdata%\\.minecraft\\assets\\indexes\\5.json")
json_decoder = json.decoder.JSONDecoder()

with open(file=mapping_path, mode="r") as f:
    json_string = f.read()
    parsed_json: dict = json_decoder.decode(json_string)['objects']
    f.close()

with open(file="mappings.txt", mode="a+") as f:
    keys: list[str] = parsed_json.keys()
    for key in keys:
        if key.startswith("minecraft/sounds/"):
            f.write(key + '\n')
        else: continue