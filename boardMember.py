import json
from datetime import datetime

# Function to convert date to string format
def format_date(date_dict):
    print(date_dict)
    date = date_dict.get('day', "")
    month = date_dict.get('month', "")
    year = date_dict.get('year', "")
    if not date or not month or not year:
        return ""
    else:
        return f"{date}-{month}-{year}"

# Read data from file
input_files = ['./streemlight/grow/people_0.json']  # Replace with the actual file path

# Initialize the result dictionary
result = {
    "info": [],
    "FOUNDER": [],
    "INDEPENDENT": []
}

# Process each entry in the data
for input_file in input_files:
    with open(input_file, 'r') as file:
        data = json.load(file)
    for entry in data:
        name = f"{entry['primaryDetailList']['name']['firstName']} {entry['primaryDetailList']['name']['lastName']}"
        
        for board_member in entry.get('boardMemberList', []):
            if board_member.get('domain') == "oxyzo.in":
                board_member_info = board_member.get('boardMemberInfo', {})
                
                result_entry = [
                    {"title": "id", "value": entry.get('id', '')},
                    {"title": "Name", "value": name},
                    {"title": "Category", "value": board_member.get('boardMemberCategory', '') + "+"},
                    {"title": "boardMemberType", "value": board_member_info.get('boardMemberType', '')},
                    {"title": "status", "value": board_member_info.get('status', '')},
                    {"title": "appointmentDate", "value": format_date(board_member_info.get('appointmentDate', {}))},
                    {"title": "Cessation date", "value": format_date(board_member_info.get('cessationDate', {}))}
                ]
                
                result["info"].append(result_entry)

                if board_member.get('boardMemberCategory') == "FOUNDER":
                    result_entry[2].update({"title":"Category","value":board_member.get('boardMemberCategory', '')})
                    result["FOUNDER"].append(result_entry)
                elif board_member.get('boardMemberCategory') == "INDEPENDENT":
                    result_entry[2].update({"title":"Category","value":board_member.get('boardMemberCategory', '')})
                    result["INDEPENDENT"].append(result_entry)
with open('./boardMembers.json', 'w') as result_file:
    json.dump(result, result_file)
# Print the result
print(result)