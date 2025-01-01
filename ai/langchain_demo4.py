from typing import Optional

from pydantic import BaseModel, Field


class Person(BaseModel):
    """关于一个人的信息。"""

    # ^ 实体Person的文档字符串
    # 这个文档字符串会被发送给LLM作为Person模式的描述，
    # 它可以帮助改善提取结果。

    # 注意：
    # 1. 每个字段都是`可选的` -- 这允许模型在无法提取时不填写该字段！
    # 2. 每个字段都有一个`描述` -- LLM会使用这个描述。
    # 一个好的描述可以帮助改善提取结果。
    name: Optional[str] = Field(default=None, description="此人的姓名")
    hair_color: Optional[str] = Field(
        default=None, description="此人的头发颜色（如果已知）"
    )
    height_in_meters: Optional[str] = Field(
        default=None, description="身高（以米为单位）"
    )

from typing import Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field

# 定义一个自定义提示来提供指令和任何额外的上下文
# 1) 你可以在提示模板中添加示例来提高提取质量
# 2) 引入额外的参数来考虑上下文（例如，包含文档的元数据）
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个专业的信息提取算法。"
            "只从文本中提取相关信息。"
            "如果你不知道要提取的属性值，"
            "则将该属性值返回为空。",
        ),
        # 请参阅如何使用参考示例来提高性能的指南
        # MessagesPlaceholder('examples'),
        ("human", "{text}"),
    ]
)

import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("请输入OpenAI API密钥: ")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

structured_llm = llm.with_structured_output(schema=Person)

text = "张伟身高1.75米，有着黑色的头发。"
prompt = prompt_template.invoke({"text": text})
res = structured_llm.invoke(prompt)

print(res)