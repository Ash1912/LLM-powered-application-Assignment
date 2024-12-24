def extract_info(query_response):
    company = query_response.get('company', 'Unknown')
    parameter = query_response.get('parameter', 'Unknown')
    start_date = query_response.get('start_date', None)
    end_date = query_response.get('end_date', None)

    start_date, end_date = get_default_dates() if not start_date or not end_date else start_date, end_date

    return {
        'company': company,
        'parameter': parameter,
        'start_date': start_date,
        'end_date': end_date
    }
