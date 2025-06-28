import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
#langchain tracing
os.environ["Langchain_api_key"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["project_key"]="QA chatbot with ollama"
#prompt temp
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistance answer the user question"),
        ("user","question :{question}") 
    ]
)
#def function
def generate_response(question,model_name,temperature,max_tokens):
    llm=Ollama(model=model_name)
    output=StrOutputParser()
    chain=prompt|llm|output
    answer=chain.invoke({"question":question})
    return answer

#streamlit function
st.title("QA CHATBOT WITH OLLAMA")
st.write("ask any thing")
#select model
model_name=st.sidebar.selectbox("select your model",["gemma3:1b","llama3.2","moondream"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("MAX-TOKEN",min_value=50,max_value=300,value=150)
#main app
st.write("ask any question")
user_input=st.text_input("enter question")

if user_input:
    response=generate_response(user_input,model_name,temperature,max_tokens)
    st.write(response)
else:
    st.write("enter input")


