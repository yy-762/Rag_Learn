
from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.document_loaders import PDFPlumberLoader
from  langchain_community.document_loaders import PDFMinerLoader

# loader = PyPDFLoader("D:/代码文件/RAG_langchain-main/RAG_langchain-main/data/baichuan.pdf")
# pages_pypdf = loader.load()
#
# print(pages_pypdf[2].page_content)
#
#
# loader = PyPDFLoader("D:/代码文件/RAG_langchain-main/RAG_langchain-main/data/baichuan.pdf",extract_images=True)
# pages_pypdf_image = loader.load()
#
# print(pages_pypdf_image[2].page_content)



loader=PDFMinerLoader("D:/代码文件/RAG_langchain-main/RAG_langchain-main/data/baichuan.pdf")
data_miner=loader.load()
print(len(data_miner))
print(data_miner[0].page_content[1590:2500])
