# 产品经理级别的agent，只输出prd文档

from pydantic import BaseModel, Field
from typing import Any, List, Dict


class PRDAgent(BaseModel):
    llm: Any = Field(
        description="llm client"
    )
    model: str = Field(
        description="model type",
        default="glm-4-flash"
    )
    messages: List[Dict[str, str]] = Field(
        default_factory=lambda: [],
        description="llm聊天消息列表"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 构建提示信息
        system_prompt = f"你是一个资深的产品经理，请根据用户的要求生成相应的产品需求文档。请生成对应PRD文档，输出以纯文本输出。"
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]

    def process_message_block(self, message: str) -> str:
        # 移除开头的代码语言标识
        if message.startswith('```'):
            first_newline = message.find('\n')
            if first_newline != -1:
                code = message[first_newline + 1:]

        # 移除结尾的 ```
        if message.endswith('```'):
            message = message[:-3]

        # 去除可能存在的首尾空白字符
        return message.strip()

    def generate_res(self, file_path: str, prompt: str) -> str:


        self.messages.append({
            "role": "user", "content": prompt
        })

        # 调用 LLM 生成代码
        completion = self.llm.chat.completions.create(
            model=self.model,
            messages=self.messages,

        )

        res = completion.choices[0].message.content

        # 处理代码块
        res = self.process_message_block(res)
        # 确保目标目录存在
        # os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 将生成的代码写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(res)

        return res

from openai import OpenAI

client = OpenAI(
  api_key="62a8a7790e3e48cfbde31f5871a0910d.z8crD3sUbCzjOU78",
  base_url="https://open.bigmodel.cn/api/paas/v4/"
)

prd_agent = PRDAgent(llm=client)
file_path = "prd.md"
prompt = "我要做一个给猎头用的人才库系统，生成一个对应的prd文档"

while True:
    prd_agent.generate_res(file_path, prompt)
    print(f"\n请在{file_path}中查看生成的PRD文档：")

    user_input = input("\n如果PRD符合要求请输入'break'退出，否则请输入新的修改建议：")
    if user_input.lower() == 'break':
        break
    else:
        prompt = user_input