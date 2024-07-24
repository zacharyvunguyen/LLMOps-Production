from fastapi import FastAPI
import uvicorn
from config import assistant_id
from pydantic import BaseModel
from openai import OpenAI
import os

# Initialize the FastAPI app
app = FastAPI()

# Initialize the OpenAI client
api_key=os.environ["OPENAI_API"]
client = OpenAI(api_key=api_key)


# Define the request body model
class Body(BaseModel):
    text: str


# Root endpoint to return a welcome message
@app.get("/")
def welcome():
    return {"message": "Hello World"}


# Home endpoint to return a welcome message for the home page
@app.get("/home")
def welcome_home():
    return {"message": "Welcome to my home page"}


# Chat endpoint to echo the input text
@app.post("/chat")
def chat(text: str):
    return {"message": text}


# Response endpoint to generate a response using the OpenAI assistant
@app.post("/response")
def generate(body: Body):
    # Extract the input text from the request body
    prompt = body.text

    # Create a new thread with the user message
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    )

    # Create and poll a run for the thread
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=assistant_id
    )

    # Retrieve the messages from the thread run
    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    # Extract and process the message content
    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")

    return {"message_content": message_content.value}


# Main entry point for running the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
