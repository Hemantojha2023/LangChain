# use google gemini as google gen ai

from langchain_google_genai import ChatGoogleGenerativeAI    # closed source google gemini chat model

from dotenv import load_dotenv 

load_dotenv() 

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result=model.invoke('What is capital of India')

print(result.content)