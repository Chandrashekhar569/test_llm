from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# call enviroment
## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. please provide responce to the user question"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain Demo with Llama3.")
input_text = st.text_input("Search your query.")




# OpenAI LLM call
llm = ollama(model="llama3")
Output_Parser = StrOutputParser()

# chain 
chain = prompt|llm|StrOutputParser

if input_text:
    st.write(chain.invoke({'question':input_text}))
