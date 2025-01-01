import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("请输入OpenAI API密钥: ")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

tagging_prompt = ChatPromptTemplate.from_template(
    """
从以下段落中提取所需信息。

仅提取'分类'函数中提到的属性。

段落内容:
{input}
"""
)


class Classification(BaseModel):
    sentiment: str = Field(description="文本的情感倾向")
    aggressiveness: int = Field(
        description="文本的攻击性程度，从1到10进行评分"
    )
    language: str = Field(description="chinese")

# LLM模型
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini").with_structured_output(
    Classification
)

inp = "我今天特别开心能认识你！相信我们一定会成为很好的朋友！"
prompt = tagging_prompt.invoke({"input": inp})
response = llm.invoke(prompt)

print(response)


