from langchain_huggingface import HuggingFaceEmbeddings


embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


documents=[
    'Delhi is the capital of India',
    'He is going to delhi for admission in college',
    'He like the culture of delhi so he want to go there',
    'He want a girlfriend from Delhi local'
]

vector=embedding.embed_documents(documents)  # for one sentance use embed_query
print(str(vector))