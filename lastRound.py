import json

input_files = ['./streemlight/oxyzo/captables.json']
result_file = 'lastRound.json'

result = {
    "keyMatrics":[]
}

def dateFormatter(date):
    print(date)
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']
    day = date.get("day","")
    month = months[date.get("month","")]
    year = date.get("year","")
    return f"{day} {month} {year}"

for input_file in input_files:
    with open(input_file) as file:
        data = json.load(file)[0]
    schema = [
            {
                "title":"Round Name",
                "value":data.get("eventName",{}).get("value","")
            },
            {
                "title":"Date",
                "value":dateFormatter(data.get("eventDate",{}).get("value",{}))
            },
            {
                "title":"Share Capital",
                "value":data.get("shareCapital",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Number of Shares issued",
                "value":data.get("noOfSharesIssued",{}).get("value","")
            },
            {
                "title":"Shareprice",
                "value":data.get("sharePrice",{}).get("value",{}).get("start",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Round size",
                "value":data.get("roundSize",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Post money Valuation",
                "value":data.get("postMoneyValuation",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Pre money Valuation",
                "value":data.get("preMoneyValuation",{}).get("value",{}).get("amount",{}).get("amount","")
            },
            {
                "title":"Total outstanding shares",
                "value":data.get("totalOutstandingShares","")
            },
            {
                "title":"Dlution",
                "value":data.get("dilutionPercentage",{}).get("value","")
            }
        ]
    for doc in schema:
        result["keyMatrics"].append(doc)

with open(result_file, 'w') as file:
    json.dump(result, file)