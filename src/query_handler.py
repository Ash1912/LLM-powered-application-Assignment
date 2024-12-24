from src.llm_integration import get_llm_response
from src.query_parser import extract_info

def handle_multiple_companies(query_response):
    companies_info = []
    companies = query_response.get('companies', [])
    for company in companies:
        company_info = extract_info(company)
        companies_info.append(company_info)
    return companies_info

def handle_query(query):
    try:
        query_response = get_llm_response(query)
        if 'error' in query_response:
            raise Exception("Error in processing the query")
        
        companies_info = handle_multiple_companies(query_response)
        return companies_info
    except Exception as e:
        print(f"Error: {str(e)}")
        return []
