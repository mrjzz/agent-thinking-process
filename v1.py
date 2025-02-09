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

completion = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    tools=function_description
)
"""
    这个create函数，可以实现参数抽取，给出函数名
"""
class FuncSet:
    def __init__(self, callable_func):
        self.funcs = callable_func  # Store as instance variable

    def __getitem__(self, name):  # Add subscript support
        return self.funcs[name]

func_set = FuncSet({
    "get_flight_info": get_flight_info
})

response = completion.choices[0].message

args = json.loads(response.tool_calls[0].function.arguments)
if response.tool_calls[0].function.name == "get_flight_info":
    res = func_set[response.tool_calls[0].function.name](args["loc_origin"], args["loc_destination"])
    print(f"出发时间是{res}")

"""
    之所以要以对象的形式，注册函数，因为每次执行函数，都需要if-else判断，代码不灵活。
    之前无法管理函数，只能用if-else的形式去判断执行哪个函数，现在可以结合openai的function calling管理函数
    这个函数可以看做一个工具，tool
"""