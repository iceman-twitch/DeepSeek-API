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

data["stream"] = True

with requests.post(API_URL, headers=headers, json=data, stream=True) as response:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            if decoded_line.startswith("data:"):
                print(decoded_line[5:])  # Process each chunk
