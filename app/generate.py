import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
load_dotenv()
TOKEN_deepseek = os.getenv("deepseek_api")

client = AsyncOpenAI(api_key=TOKEN_deepseek,
                    base_url="https://api.deepseek.com")


async def analyzing(text:str, prompt:str):
    response = await client.chat.completions.create(
        model = "deepseek-chat",
        messages = [
            {"role": "system", "content": prompt},
            {"role":"user", "content":text}
        ]
    )
    answer = response.choices[0].message.content
    return answer

async def responde(text:str, prompt:str):
    response = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    )
    answer = response.choices[0].message.content
    return answer