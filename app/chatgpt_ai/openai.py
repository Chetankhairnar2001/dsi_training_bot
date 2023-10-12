from dotenv import load_dotenv
import openai
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()
    
OPENAI_KEY = os.getenv('CHATGPT_API_KEY')

# llm = OpenAI(openai_api_key = OPENAI_KEY, model = "gpt-3.5-turbo")
chat_model = ChatOpenAI(openai_api_key = OPENAI_KEY, model = "gpt-3.5-turbo")
def chatgpt_response(prompt):
    response = chat_model.predict(prompt)
    return response

