import json

def generate_json_response(companies_info):
    return json.dumps(companies_info, indent=4)
