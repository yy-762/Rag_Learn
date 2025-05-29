from openai import OpenAI

# 使用第三方中转 API（替换成你的中转地址）
client = OpenAI(
    api_key="sk-KQW3yUay2NHaDybHYH6MuwIIZdP6PM50wjPr4ED6IsoiZ8yr",  # 你的 API Key
    base_url="https://xdaicn.top/v1",  # 替换成你的中转 API 地址
)

response = client.chat.completions.create(
    model="gpt-4-turbo",  # 模型名称（部分中转 API 可能修改了模型名，需确认）
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)