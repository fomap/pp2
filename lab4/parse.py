import json
from tabulate import tabulate

file = open("sample-data.json",)

data = json.load(file)

table = []
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    table.append([attributes["dn"], attributes["descr"], attributes["speed"], attributes["mtu"]])

print("Interface Status")
print("================================================================")
headers = ["DN", "Description", "Speed", "MTU"]
print(tabulate(table, headers=headers))



file.close()