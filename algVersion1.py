import json

def converter(filePath, resultFilePath):
    with open(filePath, "r") as file:
        global datas
        datas = json.load(file)
    converted_list = []
    datas = datas["result"]
    for data in datas:
        schema = {
            "title":data.get("name"),
            "desc":data.get("description",{}).get("short"),
            "tags":[
                {
                    "title":"website",
                    "url":data.get("domain")
                },
            ]
        }
        converted_list.append(schema)
    with open(resultFilePath, "w") as file:
        json.dump(converted_list, file)
    return converted_list

print(converter(r"C:\Users\afree\Desktop\python\1080.json", r"C:\Users\afree\Desktop\python\result.json"))