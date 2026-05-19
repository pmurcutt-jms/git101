import json

with open("json_data.json", "r") as file:
    new_user_dict = json.load(file)

print(new_user_dict)

