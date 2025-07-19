# import openai from langachain that will talk with api
from langchain_openai import OpenAI  

# import dotenv to load secret key from .env file to current file 
from dotenv import load_dotenv

# invoke function load_dotenv to load api key
load_dotenv()

# write the model name that we want to communicate of openai model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# use invoke method of langchain that will communicate with model --> just write promt in invoke it will communicate automatically
result=llm.invoke('What is the capital of India')

print(result)


# Remark OpenAI for LLM is inherits from BaseLLM to see just right click on openai go to definition 
# so now move to chatmodel that inherits from BaseChatModel 