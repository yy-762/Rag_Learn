from typing import List, Optional
from langchain.schema import SystemMessage, HumanMessage, AIMessage, BaseMessage
import requests
import os

os.environ["DEEPSEEK_API_KEY"] = "sk-9e3e0a7f58c34d9bbc9e54b93c66cbca"

class DeepSeekChat:
    def __init__(self, model: str = "deepseek-chat", temperature: float = 0.7):
        self.api_key = os.environ["DEEPSEEK_API_KEY"]
        self.model = model
        self.temperature = temperature
        self.base_url = "https://api.deepseek.com/v1/chat/completions"

    def invoke(self, messages: List[BaseMessage]) -> AIMessage:
        # 转换 LangChain Message 为 DeepSeek 格式
        deepseek_messages = []
        for msg in messages:
            if isinstance(msg, SystemMessage):
                deepseek_messages.append({"role": "system", "content": msg.content})
            elif isinstance(msg, HumanMessage):
                deepseek_messages.append({"role": "user", "content": msg.content})
            elif isinstance(msg, AIMessage):
                deepseek_messages.append({"role": "assistant", "content": msg.content})

        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "model": self.model,
            "messages": deepseek_messages,
            "temperature": self.temperature,
        }
        response = requests.post(self.base_url, json=data, headers=headers).json()
        return AIMessage(content=response["choices"][0]["message"]["content"])

# 使用示例
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Knock knock."),
    AIMessage(content="Who's there?"),
    HumanMessage(content="Orange"),
]

chat = DeepSeekChat()
res = chat.invoke(messages)
print(res.content)  # 输出: "Orange who?"