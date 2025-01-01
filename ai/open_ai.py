import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
response = model.invoke("你好！给我讲个笑话")
print(response.content)


# import getpass
# import os

# if not os.environ.get("OPENAI_API_KEY"):
#     os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# from langchain_openai import ChatOpenAI

# # 使用正确的模型名称，比如 "gpt-3.5-turbo"
# model = ChatOpenAI(model="gpt-3.5-turbo")
# # 打印输出结果
# response = model.invoke("你好！")
# print(response.content)
