from openai import OpenAI

from agent import Agent

from get_flight_info_tool import GetFlightInfoTool

get_flight_info_tool = GetFlightInfoTool()

user_prompt = "what's the next flight from london to new york"

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

agent = Agent(
    model="glm-4-flash",
    prompt=user_prompt,
    llm=client,
    tool=get_flight_info_tool
)

res = agent.run()
print(f"出发时间是{res}")