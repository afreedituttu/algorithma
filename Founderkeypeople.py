import json

input_files = ['./streemlight/grow/companies.json']
result_file = './recentInvestment.json' 

recentInvestment = []

for input_file in input_files:
    with open(input_file, 'r') as file:
        datas = json.load(file)
    for data in datas:
        peoples = data.get("employeeInfo",{}).get("employeeList","")
        for index, people in enumerate(peoples):
            schema = [
                {
                    "title":"SL No.",
                    "value":index
                },
                {
                    "title":"Name",
                    "values":people.get("name", "")
                },
                {
                    "title":"Contact info",
                    "values":people.get("emailInfo",{}).get("primaryEmail","")
                },
                {
                    "title":"Designtion",
                    "values":people.get("designation","")
                },
                {
                    "title":"Description",
                    "values":people.get("shortBio","")
                }
            ]
            recentInvestment.append(schema)
        
with open(result_file, 'w') as file:
    json.dump({"info":recentInvestment}, file)

print("SUCCESS")