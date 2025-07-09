from langchain_core.messages import HumanMessage
from langchain_openai import OpenAI
from langchain.tools import tools
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = OpenAI(temperature=0)
    tools = []
    agent_executor = create_react_agent(model, tools)

    print("你好我是ai助手，请问有什么可以帮助您的。如果想结束聊天请输入exit")

    while True:
        user_input = input("\n用户：").srtip()

        if user_input == "exit":
            print("结束聊天")
            break

        print("\nAI助手",end = " ")

        for chunk in agent_executor.stream(
                {"message": HumanMessage(user_input)}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message["content"], end="")

        print()

#
# git config --global core.autocrlf true



