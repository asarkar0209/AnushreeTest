import json

# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }

with open("data_file.json", "r") as p:
    json.load(p)


# print(data)
# with open("/home/abzooba/.PyCharmCE2019.2/config/scratches/scratch.json", "r") as read_file:
#         data = json.load(read_file)
# print(data)