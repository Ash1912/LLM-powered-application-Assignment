from src.query_handler import handle_query
from src.json_formatter import generate_json_response

def main():
    query = input("Enter your query: ")
    result = handle_query(query)
    json_output = generate_json_response(result)
    print(json_output)

if __name__ == "__main__":
    main()
