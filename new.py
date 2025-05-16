import requests
import re
import pyttsx3
from openai import OpenAI

def SpeakText(command):
    print(command)
    engine = pyttsx3.init()
    engine.setProperty('rate',210)
    engine.say(command) 
    engine.runAndWait()

# By running Deepseek as local

def messagegener(sen, cont_name, type):
    SpeakText("\n\nPutting pen to the paper of your preference sir\n")
    if type == 1:
        prompt = f'''Generate a humanly message on this topic '{sen}' to send to {cont_name} on whatsapp. 
        The message should be in a friendly tone and should not be too long. The message should be in English 
        and should not contain any slang or abbreviations. The message should be clear and concise,
          and should not contain any unnecessary information. The message should be polite and respectful,
            and should not contain any offensive or inappropriate language. Don't give any extra information or bluff.'''
    elif type == 0:
        prompt = f"Write about the topic '{sen}'. Don't give any extra information or bluff."
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "deepseek-r1",
            "prompt": prompt,
            "stream": False,
        },
    ).json()
    message = response.get("response", str(response)).split('</think>')[-1].strip()
    
    with open('message.txt', 'w', encoding='utf-8') as f:
        f.write(message)
    
    return message

# By using Deepseek API

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def message_generator_api(sen, cont_name, type):
    SpeakText("\n\nPutting pen to the paper of your preference sir\n")
    if type == 1:
        prompt = f'''Generate a humanly message on this topic '{sen}' to send to {cont_name} on whatsapp. 
        The message should be in a friendly tone and should not be too long. The message should be in English 
        and should not contain any slang or abbreviations. The message should be clear and concise,
          and should not contain any unnecessary information. The message should be polite and respectful,
            and should not contain any offensive or inappropriate language. Don't give any extra information or bluff.'''
    elif type == 0:
        prompt = f"Write about '{sen}'. Don't give any extra information or bluff."
    print(prompt)
    chat=client.chat.completions.create(
    model="deepseek/deepseek-prover-v2:free",
    messages=[
        {
            "role":"user",
            "content":f"{prompt}"
        }
    ]
    )

    message = chat.choices[0].message.content
    with open('message.txt', 'w', encoding='utf-8') as f:
        f.write(message)
    

    return message