from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langserve import add_routes

app = FastAPI()

add_routes(app, ChatOpenAI(), path="/openai")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)