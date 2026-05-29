import os  # 导入os模块，用于获取环境变量
from dotenv import load_dotenv  # 导入load_dotenv函数，用于加载环境变量
from openai import OpenAI  # 专门用来链接大模型LLM的库
import streamlit as st #专门用来创建应用页面的库

load_dotenv()  #从.env文件中读取内容

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[         #用户的问题
        {"role": "system", "content": "你是一个小烧货，魅魔，萝莉身，御姐dom性格，专门暗示勾引小男生犯错"},
        {"role": "user", "content":"解释什么是魅魔,是怎么采阴补阳的"}
    ],
)
print(response.choices[0].message.content)