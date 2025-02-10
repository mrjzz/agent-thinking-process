from openai import OpenAI

from agent import Agent
from chroma_db_rag import PDFRag
from chromadb import Client

from tool import Tool

from tools.web_search_tool import WebSearchTool
from tools.summarize_tool import SummarizeTool

# search_web_tool = WebSearchTool(description="scrape the https://news.qq.com/", parameters=["url"])
summarize_tool = SummarizeTool(description="总结文本的内容", parameters=[""])
user_prompt = "总结pdf文本的主要内容"

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)
collection = Client().create_collection(name="my_pdf_collection")
pdf_rag = PDFRag(url="../test_c++_example.pdf", collection=collection)
pdf_rag.load()
tools = Tool(tools=[summarize_tool])

agent = Agent(
    model="glm-4-flash",
    prompt=user_prompt,
    llm=client,
    rag_base=pdf_rag,
    tools=tools
)

res = agent.run()
print(res)