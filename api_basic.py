import requests

# API Endpoint (check DeepSeek's official docs for the latest URL)
API_URL = "https://api.deepseek.com/v1/chat/completions"

# Your API Key (replace with actual key)
API_KEY = "your_api_key_here"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",  # or other available models
    "messages": [
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    "temperature": 0.7  # Controls randomness (0-1)
}

response = requests.post(API_URL, headers=headers, json=data)

if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code}", response.text)
