import os
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings



def augment_prompt(query: str):#本地输入库和问题一起输入promt
  # 获取top3的文本片段
  results = vectorstore_hf.similarity_search(query, k=3)
  source_knowledge = "\n".join([x.page_content for x in results])
  # 构建prompt
  augmented_prompt = f"""Using the contexts below, answer the query.

  contexts:
  {source_knowledge}

  query: {query}"""
  return augmented_prompt
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


os.environ["OPENAI_API_KEY"] = "sk-co827MMJ5T2cbA9JLxKZgCIhKXiMvfMCXXxyuLp1MNSGBJbD"

chat = ChatOpenAI(#文本生成模型调用
    openai_api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://xdaicn.top/v1",  # 替换成你的中转 API 地址
    model='gpt-4-turbo'
)

messages = [
    SystemMessage(content="你是人工智能助手"),
    HumanMessage(content="baichuan2 有多少词汇量"),


]




loader=PyPDFLoader("https://arxiv.org/pdf/2309.10305.pdf")#加载pdf
pages = loader.load_and_split()#按页分割pdf
#print(pages[0])
#将pages分割成更小的文本快
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,#每个 chunk 最多包含 500 个字符（不是单词！）。如果文本超过 500 字符，会自动拆分。
    chunk_overlap = 50,#相邻 chunk 之间会有 50 个字符的重叠，避免语义断裂（例如一个句子被切到两个 chunk 中）。
)
docs = text_splitter.split_documents(pages)#（拆分后的 Document 对象列表，每个对象是一个 chunk）
print(len(docs))

# embed_model = OpenAIEmbeddings(
#     openai_api_key=os.environ["OPENAI_API_KEY"],
#     base_url="https://xdaicn.top/v1",  # 替换成你的中转 API 地址
#     model='text-embedding-3-small')
#只能用官方api调用该嵌入模型，换其他替代
model_name = "sentence-transformers/sentence-t5-large"
embedding = HuggingFaceEmbeddings(model_name=model_name)
vectorstore_hf = Chroma.from_documents(documents=docs, embedding=embedding , collection_name="huggingface_embed")
# vectorstore = Chroma.from_documents(documents=docs, embedding=embed_model , collection_name="openai_embed")

query="How large is the baichuan2 vocabulary?"
# result=vectorstore.similarity_search(query,k=2)
result = vectorstore_hf.similarity_search(query, k=2)


print(augment_prompt(query))
# 创建prompt
prompt = HumanMessage(
    content=augment_prompt(query)
)

messages.append(prompt)

res = chat(messages)

print(res.content)


# messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="Knock knock."),
#     AIMessage(content="Who's there?"),
#     HumanMessage(content="Orange"),
#
# ]

# messages = [
#      SystemMessage(content="你是一个专业的人工智能助手"),
#      HumanMessage(content="你知道baichuan2模型吗"),
#
#  ]
#
# baichuan2_information = [
#     "Baichuan 2是一个大规模多语言语言模型，它专注于训练在多种语言中表现优异的模型，包括不仅限于英文。这使得Baichuan 2在处理各种语言的任务时能够取得显著的性能提升。",
#     "Baichuan 2是从头开始训练的，使用了包括了2.6万亿个标记的庞大训练数据集。相对于以往的模型，Baichuan 2提供了更丰富的数据资源，从而能够更好地支持多语言的开发和应用。",
#     "Baichuan 2不仅在通用任务上表现出色，还在特定领域（如医学和法律）的任务中展现了卓越的性能。这为特定领域的应用提供了强有力的支持。"
# ]
#
# source_knowledge = "\n".join(baichuan2_information)
# print(source_knowledge)
# query = "你知道baichuan2模型吗？"
#
# prompt_template = f"""基于以下内容回答问题：
#
# 内容:
# {source_knowledge}
#
# Query: {query}"""
# prompt = HumanMessage(
#     content=prompt_template
# )
# messages.append(prompt)
#
# res = chat(messages)
# print(res.content)

# res = chat.invoke(messages)  # 使用 invoke 替代 __call__
# print(res.content)

