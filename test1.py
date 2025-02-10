from openai import OpenAI
from chromadb import Client
from pypdf import PdfReader

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

reader = PdfReader("./test_c++_example.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()

collection = Client().create_collection(name="my_pdf_collection")

collection.add(
    documents=[text],
    ids=["pdf_1"]
)

results = collection.query(
    query_texts="请概括文本的主要内容",
    n_results=3  # 检索前 3 个最相关的文档
)
# 提取检索到的文档
documents = results['documents'][0]

query = "请简要概括文档中的主要内容"
prompt = f"根据以下文档内容回答问题：{documents}\n问题：{query}"

completion = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
print(completion.choices[0].message.content)

