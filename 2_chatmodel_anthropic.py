from langchain_anthropic import ChatAnthropic   # closed source anthropic claude chatmodel

from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model='claude-3-5-sonnet-20241022')

result=model.invoke('What is the capital of India')

print(result.content)    # The capital of India is New Delhi.  also some more related to new delhi so it depends model to model
