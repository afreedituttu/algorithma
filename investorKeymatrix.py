import json

keymatrices = []

input_files = ['./oxyzo invest/alpha wave/companies.json']
result_file = './ivnestorKeymatrix.json'

for input_file in input_files:
    with open(input_file) as file:
        datas = json.load(file)
    for data in datas:
        schema = [
            {
                "title":"id",
                "value":data.get("domainProfileId","")
            },
            {
                "title":"Email id",
                "value":data.get("emailList",{})[0].get("email","")
            },
            {
                "title":"Website",
                "value":data.get("domain","")
            },
            {
                "title":"Founded Year",
                "value":data.get("foundedYear","")
            },
            {
                "title":"Location",
                "value":data.get("location",{}).get("city","")
            }
        ]
        keymatrices.append(schema)

with open(result_file, 'w') as file:
    json.dump({"keyMetrics":keymatrices}, file)

print(f'DONE, RESULT STORED TO FILE - {result_file}')