from pydantic import BaseModel, Field
from typing import Any, List, Dict
import json
import os

class CodeAgent(BaseModel):
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
        self.messages = []

    def process_code_block(self, code: str) -> str:
      # 移除开头的代码语言标识
      if code.startswith('```'):
          first_newline = code.find('\n')
          if first_newline != -1:
              code = code[first_newline + 1:]
      
      # 移除结尾的 ```
      if code.endswith('```'):
          code = code[:-3]
      
      # 去除可能存在的首尾空白字符
      return code.strip()
    def generate_code(self, file_path: str, prompt: str) -> str:
        # 构建提示信息
        system_prompt = f"你是一个代码生成助手，请根据用户的要求生成相应的代码。请只输出代码，不要包含任何解释。请在{file_path}文件中生成对应代码，输出以纯文本输出。不要用markdown，直接输出代码就行"
        
        self.messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        # 调用 LLM 生成代码
        completion = self.llm.chat.completions.create(
            model=self.model,
            messages=self.messages,

        )
        
        code = completion.choices[0].message.content

        # 处理代码块
        code = self.process_code_block(code)
        # 确保目标目录存在
        # os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # 将生成的代码写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        return code


from openai import OpenAI

client = OpenAI(
  api_key="62a8a7790e3e48cfbde31f5871a0910d.z8crD3sUbCzjOU78", 
  base_url="https://open.bigmodel.cn/api/paas/v4/"
)

code_agent = CodeAgent(llm=client)
file_path = "test.py"
prompt = "写一个函数，解决力扣上的两数之和问题"
code = code_agent.generate_code(file_path, prompt)
print(code)