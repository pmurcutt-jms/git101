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

print("Hello", user_data["name"])

