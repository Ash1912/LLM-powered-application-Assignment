import requests

def get_llm_response(query):
    url = "https://api.groq.com/v1/llama-3.1-8b-instant/query"
    headers = {
        'Authorization': 'Bearer <YOUR_API_KEY>',
        'Content-Type': 'application/json',
    }
    data = {
        "query": query,
        "model": "llama-3.1-8b-instant"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()
