import json

def converter(input_files, result_file):
    final_list = []
    for input_file in input_files:
        with open(input_file, "r") as file:
            global datas
            datas = json.load(file)
        datas = datas["result"]
        for data in datas:
            if type(data.get("name", None)) is dict:
                firstName = data.get("name", {}).get("firstName","")
                middleName = data.get("name", {}).get("middleName","")
                lastName = data.get("name", {}).get("lastName","")
                linkedin = data.get("socialProfileList", {}).get("linkedin", "")
                schema = [
                    {
                        "title":"desc",
                        "value":data.get("description",{}).get("short","")
                    },
                    {
                        "title":"name",
                        "value":' '.join(filter(None, [firstName, middleName, lastName]))
                    },
                    {
                        "title":"linkedin",
                        "value":linkedin
                    }
                ]
            else:
                schema = [
                    {
                    "title":"name",
                    "value":data.get("name", "")
                    },
                    {
                        "title":"desc",
                        "value":data.get("description",{}).get("short","")
                    },
                    {
                    "title":"website",
                    "url":data.get("domain","")
                    }
                ]
            final_list.append(schema)
    with open(result_file, "w") as file:
        json.dump(final_list, file)
    return final_list

input_files = [r"C:\Users\afree\Desktop\python\1020.json", r"C:\Users\afree\Desktop\python\1260.json", r"C:\Users\afree\Desktop\python\1080.json"]
result_file = r"./result.json"

converter(input_files, result_file)    