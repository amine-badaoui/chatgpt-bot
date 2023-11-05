import openai
from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

chat_log = [{'role': 'system',
             'content': 'You are a python tutor, completely dedicated to teach user how to learn python. \
                         you cannot answer anything else not related to python. \
                         Please provide simple instructions as the users are beginners in Python.'
             }]

@app.post("/")
async def chat(user_input: Annotated[str, Form()]):

    chat_log.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
         model='gpt-3.5-turbo',
         messages=chat_log,
         temperature=0.7
    )
    bot_response = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_response})
    return bot_response
