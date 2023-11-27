import json

investment_overview = []

input_files = ['./oxyzo invest/alpha wave/aggregation.json']
result_file = './investmentOverview.json'

for input_file in input_files:
    with open(input_file) as file:
        datas = json.load(file)
    for data in datas:
        schema = {
            "title":data.get("term",""),
            "value":data.get("value","")
        }
        investment_overview.append(schema)

with open(result_file, 'w') as file:
    json.dump( investment_overview,file)

print(f"DATA CLEANED, RESULT STORED TO FILE - {result_file}")