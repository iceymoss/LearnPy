from langchain_openai import ChatOpenAI
import getpass
import os
# 1. 导入模板类
from langchain_core.prompts import ChatPromptTemplate

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# 2. 定义系统提示模板
system_template = "Translate the following from English into {language}"
# {language} 是一个占位符，后续可以填入具体的语言，如"Chinese"、"French"等

# 3. 创建聊天提示模板
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),  # 系统角色的消息
    ("user", "{text}")           # 用户角色的消息，{text}是要翻译的文本占位符
])

model = ChatOpenAI(model="gpt-4o-mini")

response = model.invoke(prompt_template.format_messages(
    language="Chinese",
    text="Hello world"
))

print(response.content)
