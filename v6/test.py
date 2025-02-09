from openai import OpenAI

from agent import Agent

from tool import Tool

from tools.web_search_tool import WebSearchTool
from tools.summarize_tool import SummarizeTool

search_web_tool = WebSearchTool(description="scrape the https://news.qq.com/", parameters=["url"])
summarize_tool = SummarizeTool(description="总结上一条prompt内容", parameters=[""])
user_prompt = "please scrape the web info from https://news.qq.com/ and summarize the results"

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

tools = Tool(tools=[search_web_tool, summarize_tool])

agent = Agent(
    model="glm-4-flash",
    prompt=user_prompt,
    llm=client,
    tools=tools
)

res = agent.run()
print(res)