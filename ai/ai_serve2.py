import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 设置 API key
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# 初始化模型
model = ChatOpenAI(model="gpt-4o-mini")

# 1. 最简单的使用方式
response = model.invoke("你好，请介绍一下你自己")
print("基础对话：", response.content)

# 2. 使用系统提示和用户消息
messages = [
    SystemMessage(content="你是一位友善的中文助手"),
    HumanMessage(content="介绍一下北京有什么好玩的地方？")
]
response = model.invoke(messages)
print("\n带系统提示的对话：", response.content)

# 3. 多轮对话
conversation = [
    SystemMessage(content="你是一位Python编程专家"),
    HumanMessage(content="如何在Python中创建列表？"),
    # 这里可以添加 AIMessage 来包含之前的回复
    HumanMessage(content="那字典呢？")
]
response = model.invoke(conversation)
print("\n多轮对话：", response.content)

# 4. 带温度参数的调用（控制创造性）
creative_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
response = creative_model.invoke("写一个短小的科幻故事")
print("\n有创意的回答：", response.content)