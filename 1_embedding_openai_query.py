from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)


# this the the vector embedding for a single sentance. in next file we see embedding for documents
result=embedding.embed_query('Delhi is the capital of India')

print(str(result))