from fastapi import FastAPI
import openai
import os


app = FastAPI()

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def read_root():
    return {"message":"welcome to chatbot API"}

@app.post("/chat/")
def chat_with_bot(user_input:str):
    response = openai.ChatCompletion.create(model="" \
    "gpt-3.5-turbo", 
     messages=[{"role":"user", "content": user_input}]
    )
    
    return{"bot_response":response["choices"][0]["message"]["content"]}