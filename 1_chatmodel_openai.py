# to use chatmodel import ChatOpenAI
from langchain_openai import ChatOpenAI    # closed source openai chatmodel

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4', temperature=0.5)

# max_completion_tokens limits the number of words(tokens) in content(output) i.e result.content
# model=ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=10)  

#result=model.invoke('What is the capital of India')

result=model.invoke('Write a 5 line poem on cricket')
# result=model.invoke('Suggest 5 indian male names')

#print(result)

print(result.content)     # ---> The capital of India is New Delhi.  always use result.content instead of result, when using chatmodel 


# Remark when we used llm in 1_llm_demo.py the input is plain text and output also a plain text.  but when we are using chatmodels 
# it is not just a plain text it is telling more information as dictionary. and to find output we need to write result.content 
# where content is key in output of chatmodel