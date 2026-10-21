import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen3.5:4b",
    "prompt": "Explain recursion in Python.",
    "stream": False
}

response = requests.post(url, json=data)
result = response.json()
print(result["response"])