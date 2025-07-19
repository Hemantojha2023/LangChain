from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents=[
    'Delhi is the capital of India',
    'He is going to delhi for admmission in college',
    'He like the culture of delhi so he want to go there',
    'He want a girlfriend from Delhi local'
]
result=embedding.embed_documents(documents)

print(str(result))    # print(result) it automatically use str no need to write print(str(result)). both gives same output.