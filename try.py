import requests

url = "https://api.deepseek.com/v1/chat/completions"
api_key = "sk-6117fe8419b24b94b07e7d39cde29e0f"  # 替换成你的 API Key

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "中国的新能源汽车品牌有哪些？举三个最著名的，不用介绍"}],
    "temperature": 0.7,
}

response = requests.post(url, headers=headers, json=data)
print(response.json())