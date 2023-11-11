import json
import copy

base_schema = [
    {
        "title":"name",
        "value":""
    },
    {
        "title":"desc",
        "value":""
    },
    {
        "title":"webiste",
        "value":""
    },
    {
        "title":"email",
        "value":""
    },
    {
        "keyMetrics":[
            {
                "title":"website",
                "value":""
            },
            {
                "title":"Last Funding Round",
                "value":""
            },
            {
                "title":"Annual Revenue",
                "value":""
            }
        ]
    },
    {
        "Portfolio":[
            [
                {
                    "title":"imgurl",
                    "url":""
                },
                {
                    "title":"SL no.",
                    "value":""
                },
                {
                    "title":"Location",
                    "value":""
                },
                {
                    "title":"Year",
                    "value":""
                },
                {
                    "title":"Funding",
                    "value":""
                },
                {
                    "title":"Company stage",
                    "value":""
                },
                {
                    "title":"Short description",
                    "value":""
                }
            ]
        ]
    }
]

def schema_updater(name, desc, website):
    schema = copy.deepcopy(base_schema)
    schema[0].update({"value":name})
    schema[1].update({"value":desc})
    schema[2].update({"value":website})

    return schema

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
            name = ""
            description = ""
            website = ""

            if type(data.get("name", None)) is dict:
                first_name = data.get("name", {}).get("firstName", "")
                middle_name = data.get("name", {}).get("middleName", "")
                last_name = data.get("name", {}).get("lastName", "")
                name = ' '.join(filter(None, [first_name, middle_name, last_name]))
                website = data.get("domain", "")
                description = data.get("summary", "")

                if len(description) == 0:
                    description = data.get("description", {}).get("short", "")
                if len(website) == 0:
                    website = data.get("socialProfileList", {}).get("linkedin", "")
            else:
                name = data.get("name", "")
                description = data.get("description", {}).get("short", "")
                website = data.get("domain", "")
            schema = schema_updater(name, description, website)
            
            print(schema)
            print('\n\n')

            final_list.append(schema)
    with open(result_file, "w") as file:
        json.dump(final_list, file)
    return final_list

input_files = [r"C:\Users\afree\Desktop\python\1020.json", r"C:\Users\afree\Desktop\python\1260.json", r"C:\Users\afree\Desktop\python\1080.json"]
result_file = r"./result.json"

converter(input_files, result_file)    