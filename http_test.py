import httpx

# 创建一个自定义的 HTTP 客户端
client = httpx.Client(http2=True)

# 打印请求和响应的详细信息
client = httpx.Client(http2=True, event_hooks={'request': [print_request], 'response': [print_response]})

def print_request(request):
    print(f"Request: {request.method} {request.url}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.content}")

def print_response(response):
    print(f"Response Status: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Body: {response.text}")

# 使用自定义客户端进行请求
try:
    response = client.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
    print(response.text)
except Exception as e:
    print(f"Error: {e}")