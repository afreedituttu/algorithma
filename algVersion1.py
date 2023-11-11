import json

def converter(input_files, result_file):
    # to store the datas of each investor
    final_list = []

    # to navigate through each input files
    for input_file in input_files:
        with open(input_file, "r") as file:
            global datas
            datas = json.load(file)
        datas = datas["result"]

        # to navigate through each investor data
        for data in datas:

            # institutional and private investors can be sepearated by their name format for using different schemes for each
            # private investors has their name in the form of dict
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
            # institutional investors have their name as in the form of string
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