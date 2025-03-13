from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    api_key="65b0348119a6b858ee16dda43ede5a8c.DFnYvPKSZDO5ciKL",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="glm-4-flash",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed

print(event)