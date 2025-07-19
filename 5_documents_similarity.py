from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query='Tell me about Sachin.'

doc_embeddings=embedding.embed_documents(documents)

query_embeddings=embedding.embed_query(query)

# since doc_embeddings is 2D and query_embeddings is 1D so make it 2D first using [] and we need first element of score so use [0]
scores=cosine_similarity([query_embeddings], doc_embeddings)[0]  

# since it is sorted increasing order high similarly will place in last so used [-1] that i need which close to query
# used it enumerate(scores) to convert into tuple according to index of documents element and similarity so that if we sort it, 
# it won't effect the indexing of similarity. i.e after sorting index and and similarity score together in tuple. 
# before sorting store it into list. and key=lambda x : x[1] used [1] for score from tuple 
index, score=sorted(list(enumerate(scores)), key=lambda x : x[1])[-1]

print(query)
print(documents[index])

print('Similarity score is :',score)

