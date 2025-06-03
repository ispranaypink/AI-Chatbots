from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_core.runnables import RunnableLambda
from langchain_community.llms import Ollama
from dotenv import  load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API Server"
)


model = ChatOpenAI()
llm = Ollama(model = "tinyllama")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

essay_chain = prompt1 | model
poem_chain = prompt2 | llm

add_routes(
    app,
    essay_chain,
    path = "/essay"
)

add_routes(
    app,
    poem_chain,
    path = "/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host = "localhost", port = 8000)