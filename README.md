# LLM-powered-application-Assignment

# LLM-Powered Performance Metrics Application

## Setup Instructions

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
    ```
3. Run the application
    ```bash
    python run.py
    ```
4. Enter a query to see the performance metrics in JSON format.

### Example Query

    ```bash
    "What was the revenue of Flipkart for 2023?"
    ```

The output will be a structured JSON with company name, performance metric, and date range.


## Project Directory

```bash
llm-powered-application-assignment/
│
├── data/
│   └── sample_queries.json      # Optional: Sample queries for testing
│
├── src/
│   ├── __init__.py              # To mark the folder as a package
│   ├── llm_integration.py       # Interact with LLM API
│   ├── date_utils.py            # Date parsing and manipulation
│   ├── query_parser.py          # Extract info from LLM responses
│   ├── query_handler.py         # Handle multiple companies, errors, etc.
│   └── json_formatter.py        # Format output as JSON
│
├── tests/
│   ├── test_llm_integration.py  # Unit tests for LLM interaction
│   ├── test_query_parser.py     # Unit tests for parsing the query
│   └── test_json_formatter.py   # Unit tests for the JSON response
│
├── requirements.txt            # Project dependencies
├── run.py                      # Main script to run the application
└── README.md                   # Project instructions and documentation
```


