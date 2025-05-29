from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("D:/代码文件/RAG_langchain-main/RAG_langchain-main/data/baichuan.pdf")
pages_pypdf = loader.load()

print(pages_pypdf[2].page_content)
