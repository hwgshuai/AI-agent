from langchain.chat_models import init_chat_model
# 获取环境变量、操作文件路径等，这里主要用它来获取环境变量
import os
from dotenv import load_dotenv

load_dotenv()

# 从环境变量中读取API KEY
api_key = os.getenv('DEEPSEEK_API_KEY')
print((api_key))
api_key = "sk-6117fe8419b24b94b07e7d39cde29e0f"
base_url = "https://api.deepseek.com/"

model = init_chat_model(
    model='deepseek-chat',  # 指定使用的模型名称，需与平台支持的模型名匹配
    # 以下为传入 DeepSeek 模型需要的额外参数，比如 api_key、base_url 等
    api_key=api_key,
    base_url=base_url,
    temperature=1.3,  # 示例参数，控制生成文本的随机性
    max_tokens=520,  # 示例参数，控制生成文本的最大 token 数
)

print("mode:", type(model))
print("欢迎使用聊天助手！输入您的问题开始聊天，输入'exit'退出。")

while True:
    user_input = input("您: ")

    # 检查用户是否想退出
    if user_input.lower() == 'exit':
        print("再见！")
        break

    # 获取模型响应
    try:
        response = model.invoke(user_input)
        print("助手:", response.content)
    except Exception as e:
        print("发生错误:", e)