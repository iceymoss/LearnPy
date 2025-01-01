from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 嵌入向量
from langchain_openai import OpenAIEmbeddings
import getpass
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
# 运行异步函数
import asyncio

# 这里我们将针对 PDF 文档构建一个搜索引擎。这将使我们能够检索 PDF 中与输入查询相似的段落。

# documents = [
#     Document(
#         page_content="Dogs are great companions, known for their loyalty and friendliness.",
#         metadata={"source": "mammal-pets-doc"},
#     ),
#     Document(
#         page_content="Cats are independent pets that often enjoy their own space.",
#         metadata={"source": "mammal-pets-doc"},
#     ),
# ]

file_path = "/Users/iceymoss/Desktop/2024论文/定稿版/V6.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

# print(len(docs))

# print(f"{docs[0].page_content[:200]}\n")
# print(docs[0].metadata)

#处理文本
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # 每个块的最大字符数
    chunk_overlap=100,  # 块之间的重叠字符数
    add_start_index=True  # 添加起始索引到元数据
)
all_splits = text_splitter.split_documents(docs)

# 1. 打印分割后的文档数量
# print(f"文档被分割成了 {len(all_splits)} 个部分\n")

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# 生成文本嵌入的模型
# vector_1 = embeddings.embed_query(all_splits[0].page_content)
# vector_2 = embeddings.embed_query(all_splits[1].page_content)

# 模型长度
# assert len(vector_1) == len(vector_2)
# print(f"Generated vectors of length {len(vector_1)}\n")
# print(vector_1[:10])

vector_store = InMemoryVectorStore(embeddings)
ids = vector_store.add_documents(documents=all_splits)

# 同步查询
# results = vector_store.similarity_search(
#     "PostgreSQL是什么？"
# )

# 带分数的查询
# results = vector_store.similarity_search_with_score("PostgreSQL是什么？")
# doc, score = results[0]
# print(f"Score: {score}\n")
# print(doc)

# 向量查询
embedding = embeddings.embed_query("杨旷是什么？")

results = vector_store.similarity_search_by_vector(embedding)
print(results[0])

# 将查询代码包装在异步函数中
# async def perform_search():
#     results = await vector_store.asimilarity_search("杨旷是谁?")
#     print(results[0])

# # 运行异步函数
# asyncio.run(perform_search())


from typing import List

from langchain_core.documents import Document
from langchain_core.runnables import chain


@chain
def retriever(query: str) -> List[Document]:
    return vector_store.similarity_search(query, k=1)


results = retriever.batch(
    [
        "杨旷是什么学校的?",
        "杨旷的专业是什么?",
    ],
)

print(results)