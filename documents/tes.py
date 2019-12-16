import json

with open("rows.txt", "r") as f:
    jsonData = json.load(f)
"""
result = []
for txt in jsonData["list"]:
    data = {}
    with open(txt, "rb") as f:
        data[txt] = f.read()
    result.append(data)
jsonData["list"] = result
"""
with open('rows.txt','r') as f:
    jsonObject = json.load(f)
    print(jsonObject)

