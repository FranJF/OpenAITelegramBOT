import openai
import telegram

pregunta:str = "¿Quien es el presidente de Estados Unidos?"

openai.api_key = "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"
completion = openai.Completion.create(engine="text-davinci-003", prompt=pregunta, max_tokens=2048)
respuesta:str = completion.choices[0].text
print(respuesta)




TELEGRAM_BOT_KEY_API = "6247474269:AAH4Jh8GNrQw8HWFXScsTIsWnAtJUdtuDKw"

async def main():
    bot = telegram.Bot(TELEGRAM_BOT_KEY_API)
    async with bot:
        update = await bot.get_updates()[0]
        chat_id:int = update.message.from_user.id
        await bot.send_message(text='Hi John!', chat_id=chat_id)
