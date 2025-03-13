from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)
class FormatOutput(BaseModel):
    intermediate_answer: str
    final_answer: str
completion = client.beta.chat.completions.parse(
    model="glm-4-flash",
    response_format=FormatOutput,
    messages=[
        {
            "role": "user",
            "content": "how old are the us president?"
        }
    ],
    # stop="\nIntermediate answer:"
)
math_response = completion.choices[0].message

math_response = math_response.parsed
print(math_response.intermediate_answer)
print(math_response.final_answer)