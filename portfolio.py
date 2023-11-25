import json
import math

millnames = ['',' Thousand',' M',' B',' Trillion']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
    int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    money = '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
    return f'${money}'

portfolios = []

result_file = './portfolio.json'
input_files = ['./companies/021 Capital/companies_1.json']

for input_file in input_files:
    with open(input_file, 'r') as file:
        datas = json.load(file)
    for index, data in enumerate(datas):
        schema = [
            {
                "title":"SL no.",
                "value":index
            },
            {
                "title":"Name",
                "value":data.get('name',"")
            },
            {
                "title":"Location",
                "value":data.get("location",{}).get("city","")
            },
            {
                "title":"Year",
                "value":data.get("foundedYear","")
            },
            {
                "title":"Funding",
                "value":millify(data.get("totalMoneyRaised",{}).get("totalAmount",{}).get("amount",""))
            },
            {
                "title":"Company Stage",
                "value":data.get("stage","")
            },
            {
                "title":"Short description",
                "value":data.get("description",{}).get("short","")
            }
        ]
        portfolios.append(schema)

with open(result_file, 'w') as file:
    json.dump(portfolios, file)