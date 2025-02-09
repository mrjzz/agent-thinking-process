from openai import OpenAI
import json

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

function_description = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_info",
            "description": "get flight info between two airports",
            "parameters": {
                "type": "object",
                "properties": {
                    "loc_origin": {
                        "type": "string",
                        "description": ""
                    },
                    "loc_destination": {
                        "type": "string",
                        "description": ""
                    }
                },
                "required": ["loc_origin", "loc_destination"]
            },
        }

    }
]

user_prompt = "what's the next flight from london to new york"


def get_flight_info(loc_origin, loc_destination):
    print(f"出发地是{loc_origin}")
    print(f"终点是{loc_destination}")
    return "早上七点"

"""(v1.py)
    这个create函数，可以实现参数抽取，给出函数名
"""


# v2.py 修改FuncSet为ToolSet
"""（v2.py）
    分析执行一个agent，普遍的框架应该是怎么样的。需要有prompt，llm，tool，memory，
    目前的执行过程是，
        1，调用openai的create函数，根据prompt，返回tool所需要的参数。
        2，执行tool，返回结果
    我期望的调用过程：
        1，构建一个对象
        2，调用对象的run函数。
    因此，这时需要一个agent类。
"""


# v2.py 试着写一个Agent类

# v3.py 精修Agent的逻辑
"""(v3.py)
    create函数里面的tools=function_description传参，要改一下，单独封装一个tool。
    
"""

class GetFlightInfoTool:
    def get_description(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_flight_info",
                    "description": "get flight info between two airports",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "loc_origin": {
                                "type": "string",
                                "description": ""
                            },
                            "loc_destination": {
                                "type": "string",
                                "description": ""
                            }
                        },
                        "required": ["loc_origin", "loc_destination"]
                    },
                }

            }
        ]
    def __init__(self):
        self.funcs = {
            "get_flight_info": get_flight_info
        }
    def __getitem__(self, item):
        return self.funcs[item]

class Agent:
    def __init__(self, prompt, llm, tool, model):
        self.prompt = prompt
        self.llm = llm  # llm是一个client
        self.tool = tool
        self.model = model

    def run(self):
        completion = client.chat.completions.create(
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
        args = json.loads(response.tool_calls[0].function.arguments)
        res = self.tool.funcs[response.tool_calls[0].function.name](args["loc_origin"], args["loc_destination"])
        print(f"出发时间是{res}")

get_flight_info_tool = GetFlightInfoTool()
# v2.py 试着生成一个Agent类对象
agent = Agent(
    model="glm-4-flash",
    prompt=user_prompt,
    llm=client,
    tool=get_flight_info_tool
)
agent.run()

"""(v1.py)
    之所以要以对象的形式，注册函数，因为每次执行函数，都需要if-else判断，代码不灵活。
    之前无法管理函数，只能用if-else的形式去判断执行哪个函数，现在可以结合openai的function calling管理函数
    这个函数可以看做一个工具，tool
"""