from dotenv import load_dotenv
import openai
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()
    
openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
        messages=[{'role':"user","content":prompt}])
    response = completion.choices[0].message.content
    if len(response) <= 2000:
        return response
    else:
        return response[:1997] + "..."
