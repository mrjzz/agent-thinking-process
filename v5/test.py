from openai import OpenAI

from agent import Agent

from get_flight_info_tool import GetFlightInfoTool
from book_flight_tool import BookFlightTool

from tool import Tool

get_flight_info_tool = GetFlightInfoTool()
book_flight_tool = BookFlightTool()

user_prompt = "what's the next flight from london to new york and book it"

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

tools = Tool(tools=[get_flight_info_tool, book_flight_tool])

agent = Agent(
    model="glm-4-flash",
    prompt=user_prompt,
    llm=client,
    tools=tools
)

res = agent.run()
print(res)