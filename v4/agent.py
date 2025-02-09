
import json

"""
    Agent负责整个各个组件，并执行prompt和相关指令。
"""
class Agent:
    def __init__(self, prompt, llm, tool, model):
        self.prompt = prompt
        self.llm = llm  # llm是一个client
        self.tool = tool
        self.model = model

    def run(self):
        completion = self.llm.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": self.prompt
                }
            ],
            tools=self.tool.get_description()
        )
        response = completion.choices[0].message
        func_param = response.tool_calls[0].function
        args = json.loads(func_param.arguments)
        res = self.tool.call_tool(args)
        return res
