import json

input_files = ['./streemlight/grow/captables.json']
result_file = './shareHoldPatter.json'

result = {
    "info": [
        [
            {
                "title":"Name",
                "value":""
            },
            {
                "title":"shareholderGroup",
                "value":"Founder +"
            },
            {
                "title":"Pre round Holding",
                "value":""
            },
            {
                "title":"Post round Holding",
                "value":""
            },
            {
                "title":"Increase in Share capital",
                "value":""
            },
            {
                "title":"Post round cumulative investment",
                "value":""
            },
            {
                "title":"Cumulative realised Returns",
                "value":""
            },
            {
                "title":"Shares Bought/Allocated",
                "value":""
            }
        ],
        [
            {
                "title":"Name",
                "value":""
            },
            {
                "title":"shareholderGroup",
                "value":"Parent Entity +"
            },
            {
                "title":"Pre round Holding",
                "value":""
            },
            {
                "title":"Post round Holding",
                "value":""
            },
            {
                "title":"Increase in Share capital",
                "value":""
            },
            {
                "title":"Post round cumulative investment",
                "value":""
            },
            {
                "title":"Cumulative realised Returns",
                "value":""
            },
            {
                "title":"Shares Bought/Allocated",
                "value":""
            }
        ],
        [
            {
                "title":"Name",
                "value":""
            },
            {
                "title":"shareholderGroup",
                "value":"Enterprise +"
            },
            {
                "title":"Pre round Holding",
                "value":""
            },
            {
                "title":"Post round Holding",
                "value":""
            },
            {
                "title":"Increase in Share capital",
                "value":""
            },
            {
                "title":"Post round cumulative investment",
                "value":""
            },
            {
                "title":"Cumulative realised Returns",
                "value":""
            },
            {
                "title":"Shares Bought/Allocated",
                "value":""
            }
        ],
        [
            {
                "title":"Name",
                "value":""
            },
            {
                "title":"shareholderGroup",
                "value":"Angel +"
            },
            {
                "title":"Pre round Holding",
                "value":""
            },
            {
                "title":"Post round Holding",
                "value":""
            },
            {
                "title":"Increase in Share capital",
                "value":""
            },
            {
                "title":"Post round cumulative investment",
                "value":""
            },
            {
                "title":"Cumulative realised Returns",
                "value":""
            },
            {
                "title":"Shares Bought/Allocated",
                "value":""
            }
        ],
    ],
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
                "value":data.get("nameInfo",{}).get("name",{}).get("value","") or data.get("nameInfo",{}).get("legalName",{}).get("value","") or data.get("parentInfo",{}).get("name","") or data.get("nameInfo",{}).get("companyName",{})
            },
            {
                "title":"shareholderGroup",
                "value":data.get("shareholderGroup","")
            },
            {
                "title":"Pre round Holding",
                "value":data.get("preRoundHolding",{}).get("value","")
            },
            {
                "title":"Post round Holding",
                "value":data.get("postRoundHolding",{}).get("value","")
            },
            {
                "title":"Increase in Share capital",
                "value":data.get("currentRoundInvestment",{}).get("value",{}).get("amount",{}).get("amount","") or data.get("increaseInShareCapital",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Post round cumulative investment",
                "value":data.get("postRoundCumulativeInvestment",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Cumulative realised Returns",
                "value":data.get("unrealisedReturn",{}).get("value",{}).get("amount",{}).get("amount","") or data.get("cumulativeRealisedReturn",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Shares Bought/Allocated",
                "value":data.get("shareBoughtOrAllocated",{}).get("value","")
            }
        ]

        if data.get("shareholderGroup","") == 'Founder':
            result['Founder'].append(schema)
        elif data.get("shareholderGroup","") == 'Parent Entity':
            result['Parent Entity'].append(schema)
        elif data.get("shareholderGroup","") == 'Enterprise':
            result['Enterprise'].append(schema)
        elif data.get("shareholderGroup","") == 'Angel':
            result['Angel'].append(schema)
        elif data.get("shareholderGroup","") == 'Total':
            result['Total'].append(schema)
        else:
            pass

with open(result_file, 'w') as file:
    json.dump(result, file)

print('DONE')