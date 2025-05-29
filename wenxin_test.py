import requests
import json

# 你的文心一言API Key和Secret（需要在百度AI开放平台申请）
API_KEY = '你的API_KEY'
API_SECRET = '你的API_SECRET'


# 获取Access Token的函数（百度API需要先获取token）
def get_access_token(api_key, api_secret):
    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': api_secret
    }
    response = requests.post(token_url, params=params)
    if response.status_code == 200:
        token_info = response.json()
        return token_info['access_token']
    else:
        raise Exception(f"获取access_token失败: {response.text}")


# 调用文心一言接口的函数
def call_wenxin_yiyan(access_token, prompt):
    api_url = f"https://wenxin.baidu.com/moduleApi/portal/api/rest/1.0/ernie/engine/v1/chat/completions?access_token={access_token}"

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "model": "ernie-bot",  # 具体模型名称可根据官方文档替换
        "max_tokens": 2048,
        "temperature": 0.7
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"调用文心一言API失败: {response.text}")


if __name__ == "__main__":
    try:
        token = get_access_token(API_KEY, API_SECRET)
        prompt_text = "你好，文心一言！"
        result = call_wenxin_yiyan(token, prompt_text)
        print("文心一言回复：", result['choices'][0]['message']['content'])
    except Exception as e:
        print("出错了:", e)
