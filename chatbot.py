from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = ChatMistralAI(
    model="ministral-8b-2512",temperature=0,
    api_key="zzDVO6qrHgx5IWrgugpXcaBvCUvecxDc"   # correct key
)
message=[
    SystemMessage(content="You are funny AI agent")
]
print("--------------------welcome to 0 exit to the apllication-----------------")
while True:
    
    prompt=input("You:")
    message.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot :",response.content)
print(message)