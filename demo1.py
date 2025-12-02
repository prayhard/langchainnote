import os
from dotenv import load_dotenv
from langchain.agents import  create_agent
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
load_dotenv()
llm=ChatOpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
    api_key=SecretStr(os.environ['API_KEY'])
)
#直接调用大模型
print(llm.invoke("你是谁").content)
agent=create_agent(llm,system_prompt="你叫楼兰，是我的专属学习伙伴")

#封装agent,调用大模型
print(agent.invoke(
    {"messages":[{'role':'user','content':'你是谁'}]}
)["messages"])
