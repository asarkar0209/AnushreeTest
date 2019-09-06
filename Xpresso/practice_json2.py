import json

data = {
    "uid":"asarkar",
    "pwd":"hellolife",
    "firstName":"Anushree",
    "lastName":"Sarkar",
    "email":"anushree.sarkar@abzooba.com"

    }

with open("create_user1.json", "w") as write_file:
    json.dump(data, write_file)