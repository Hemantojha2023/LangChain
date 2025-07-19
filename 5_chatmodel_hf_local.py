import os 
os.environ['HF_HOME']='D:/huggingface_cache'
# os.environ['HF_DATASETS_CACHE'] = 'D:/huggingface_cache/datasets' 


from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    model_id='HuggingFaceH4/zephyr-7b-beta',
    task='text-generation'        # when use local machine
)

model=ChatHuggingFace(llm=llm)
result=model.invoke('Write a poem on a beautiful girl')

print(result.content)

# Remark when we use hugging face model through api and if using chat model i.e ChatHuggingFace then use task='chat-completion' but if we use 
# chat model on local machine , we use pipeline that does not support chat-completion then use task='text-generation' or 'text2text-generation'
# 'text-classification'. zephyr-7b-beta is based on Mistral, a decoder-only (GPT-like) model. 
# Zephyr, a chat-optimized model — not just a plain text generation model 