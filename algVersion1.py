import json

def converter(input_files, result_file):
    final_list = []
    for input_file in input_files:
        with open(input_file, "r") as file:
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
                    }
                ]
            }
            converted_list.append(schema)
        for data in converted_list:
            final_list.append(data)
    with open(result_file, "w") as file:
        json.dump(final_list, file)
    return final_list

input_files = [r"C:\Users\afree\Desktop\python\1020.json", r"C:\Users\afree\Desktop\python\1260.json"]
result_file = r"./result.json"

converter(input_files, result_file)    