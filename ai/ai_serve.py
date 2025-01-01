import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Translate the following from English into chinese"),
    HumanMessage("hi!"),
]

# res = model.invoke(messages)

# res = model.invoke("Hello")

# res = model.invoke([{"role": "user", "content": "Hello"}])

# res = model.invoke([HumanMessage("Hello")])

# print(res.content)

for token in model.stream(messages):
    print(token.content, end="|")

