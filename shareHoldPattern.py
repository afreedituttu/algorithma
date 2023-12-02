import json

input_files = ['./streemlight/oxyzo/captables.json']
result_file = './shareHoldPatter.json'

result = {
    "info": [],
    "Founder": [],
    "Parent Entity": [],
    "Enterprise" : [],
    "Angel" : [],
    "Total" : []
}

for input_file in input_files:
    with open(input_file, 'r') as file:
        datas = json.load(file)[0]['shareHolderList']
    for data in datas:
        schema = [
            {
                "title":"Name",
                "value":data.get("nameInfo",{}).get("name",{}).get("value","") or data.get("nameInfo",{}).get("legalName",{}).get("value","") or data.get("parentInfo",{}).get("name","")
            },
            {
                "title":"shareholderGroup",
                "value":data.get("shareholderGroup","")
            },
            {
                "title":"Pre round Holding",
                "value":data.get("preRoundHolding","")
            },
            {
                "title":"Post round Holding",
                "value":data.get("postRoundHolding","")
            },
            {
                "title":"Increase in Share capital",
                "value":data.get("currentRoundInvestment",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Post round cumulative investment",
                "value":data.get("postRoundCumulativeInvestment",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Cumulative realised Returns",
                "value":data.get("unrealisedReturn",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Shares Bought/Allocated",
                "value":data.get("shareBoughtOrAllocated","")
            }
        ]

        if data.get("shareholderGroup","") == 'Founder':
            result['Founder'].append(schema)
        elif data.get("shareholderGroup","") == 'Parent Entity':
            result['Parent Entity'].append(schema)
        elif data.get("shareholderGroup","") == 'Enterprise':
            result['Parent Entity'].append(schema)
        elif data.get("shareholderGroup","") == 'Angel':
            result['Parent Entity'].append(schema)
        elif data.get("shareholderGroup","") == 'Total':
            result['Parent Entity'].append(schema)
        else:
            pass

        schema[1].update({
                "title":"shareholderGroup",
                "value":data.get("shareholderGroup","") + ' +'
            })
        result["info"].append(schema)

with open(result_file, 'w') as file:
    json.dump(result, file)

print('DONE')