import json

print("Hello!")

name = input("What is your name?")
age = int(input("What is your age?"))
street_num = int(input("What is your house number?"))
post_code = input("What is your postcode?")

user_data = {"name" : name,
             "age" : age,
             "street_num" : street_num,
             "post_code" : post_code }

with open("json_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

with open("json_data.json", "r") as file:
    new_user_dict = json.load(file)


print(new_user_dict)

