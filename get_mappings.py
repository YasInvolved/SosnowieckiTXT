import re, os, json

mapping_path: str = os.path.expandvars("%appdata%\\PrismLauncher\\assets\\indexes\\17.json")
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