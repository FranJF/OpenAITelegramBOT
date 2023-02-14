import os
import asyncio
import openai
import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_KEY_API = os.getenv("TELEGRAM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# pregunta:str = "¿Quien es el presidente de Estados Unidos?"

# openai.api_key = OPENAI_API_KEY
# completion = openai.Completion.create(engine="text-davinci-003", prompt=pregunta, max_tokens=2048)
# respuesta:str = completion.choices[0].text
# print(respuesta)

async def main():
    bot = telegram.Bot(TELEGRAM_BOT_KEY_API)
    print(bot)
    async with bot:
        update = await bot.get_updates()[0]
        chat_id:int = update.message.from_user.id
        await bot.send_message(text='Hi John!', chat_id=chat_id)
        print(chat_id)

asyncio.run(main())
