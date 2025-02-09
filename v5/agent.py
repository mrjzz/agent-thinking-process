
import json

"""
    Agent负责整个各个组件，并执行prompt和相关指令。
"""
class Agent:
    def __init__(self, prompt, llm, tools, model):
        self.prompt = prompt
        self.llm = llm  # llm是一个client
        self.tools = tools
        self.model = model
        self.messages = [
            {
                "role": "user",
                "content": self.prompt
            }
        ]

    def run(self):
        # completion = self.llm.chat.completions.create(
        #     model=self.model,
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": self.prompt
        #         }
        #     ],
        #     tools=self.tools.get_description()
        # )
        # response = completion.choices[0].message
        # func_param = response.tool_calls[0].function
        # args = json.loads(func_param.arguments)
        # res = self.tools.call_tool(args)
        # return res

        for tool in self.tools.tools:
            completion = self.llm.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=tool.get_description()
            )
            response = completion.choices[0].message
            func_param = response.tool_calls[0].function
            args = json.loads(func_param.arguments)
            res = tool.call_tool(args)
            self.messages.append({
                "role": "user",
                "content": res
            })
        res = self.messages[-1]["content"]
        return res
