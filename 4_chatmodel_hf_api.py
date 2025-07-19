from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 


from dotenv import load_dotenv 

import os

load_dotenv() 

# load model from hugging face and tell the task using huggingfaceendpoint function
llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task='chat-completion',
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),   # use this in case of hugging face
    max_new_tokens=5
)
model = ChatHuggingFace(llm=llm)

result=model.invoke('What is the capital of India')

print(result.content)

# Remark: Since we are using ChatHuggingFace for chat models so be ensure that task should be chat-completion means conversation 
# not the task is text-generation. text-generation and chatting both different. and also be ensure that you are using chat model in 
# repo_id parametern don't use LLM