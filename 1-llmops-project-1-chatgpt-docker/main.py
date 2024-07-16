from fastapi import FastAPI
import uvicorn
from config import api_key, assistant_id
from pydantic import BaseModel
app = FastAPI()
from openai import OpenAI
client = OpenAI(api_key=api_key)
class Body(BaseModel):
    text: str
@app.get("/")
def welcome():
    return {"message": "Hello World"}

@app.get("/home")
def welcome_home():
    return {"message": "Welcome to my home page"}

@app.post("/chat")
def chat(text: str):
    return {"message": text}


@app.post("/response")
def generate(body: Body):
    prompt = body.text
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=assistant_id
    )

    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")

    return {"message_content": message_content.value}


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)
