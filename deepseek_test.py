import requests
import json

# 你的DeepSeek API密钥
API_KEY = 'sk-9e3e0a7f58c34d9bbc9e54b93c66cbca'

# DeepSeek接口URL（请替换为官方文档提供的实际接口地址）
API_URL = 'https://api.deepseek.com/v1/chat/completions'  # 示例地址

def call_deepseek_api(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    data = {
        "model": "deepseek-chat",   # 根据DeepSeek提供的模型名称替换
        "messages": [
            {"role": "user", "content": prompt}
        ]
        # 根据DeepSeek文档添加其他请求参数
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        # 假设返回格式和OpenAI类似，提取回复内容
        return result['choices'][0]['message']['content']
    else:
        raise Exception(f"请求失败，状态码：{response.status_code}，信息：{response.text}")

if __name__ == "__main__":
    user_input = "你好，DeepSeek！"
    try:
        reply = call_deepseek_api(user_input)
        print("DeepSeek回复：", reply)
    except Exception as e:
        print("调用DeepSeek API出错:", e)
