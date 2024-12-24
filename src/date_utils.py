from datetime import datetime, timedelta
from dateutil import parser

def get_default_dates():
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)
    return start_date.isoformat(), end_date.isoformat()

def parse_date(date_string):
    return parser.parse(date_string).isoformat() if date_string else datetime.today().isoformat()
