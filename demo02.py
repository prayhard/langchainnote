import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from pydantic import SecretStr
from typing_extensions import NotRequired

load_dotenv()

llm = ChatOpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
    api_key=SecretStr(os.environ["API_KEY"]),
)

class State(TypedDict):
    author:NotRequired[str]
    joke:NotRequired[str]

def author_node(state:State):
    prompt='帮我推荐一位受人们欢迎的作家。只需要给出作家的名字即可。'
    author=llm.invoke(prompt)
    return {'author':author.content}

def joke_node(state:State):
    prompt=f"用作家{state['author']}的风格，写一个100字以内的笑话"
    joke=llm.invoke(prompt)
    return {'joke':joke.content}

builder = StateGraph(State)
builder.add_node(author_node)
builder.add_node(joke_node)

builder.add_edge(START, "author_node")
builder.add_edge("author_node", "joke_node")
builder.add_edge("joke_node", END)

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)
print(graph)

