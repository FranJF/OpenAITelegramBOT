import os
import asyncio
import openai
import telegram
from telegram.error import Forbidden, NetworkError
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_KEY_API = os.getenv("TELEGRAM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# pregunta:str = "¿Quien es el presidente de Estados Unidos?"

# openai.api_key = OPENAI_API_KEY
# completion = openai.Completion.create(engine="text-davinci-003", prompt=pregunta, max_tokens=2048)
# respuesta:str = completion.choices[0].text
# print(respuesta)
async def main() -> None:
    """Run the bot."""
    # Here we use the `async with` syntax to properly initialize and shutdown resources.
    async with telegram.Bot(TELEGRAM_BOT_KEY_API) as bot:
        # get the first pending update_id, this is so we can skip over it in case
        # we get a "Forbidden" exception.
        try:
            update_id = (await bot.get_updates())[0].update_id
        except IndexError:
            update_id = None

        # logger.info("listening for new messages...")
        while True:
            try:
                update_id = await echo(bot, update_id)
            except NetworkError:
                await asyncio.sleep(1)
            except Forbidden:
                # The user has removed or blocked the bot.
                update_id += 1


async def echo(bot, update_id: int) -> int:
    """Echo the message the user sent."""
    # Request updates after the last update_id
    updates = await bot.get_updates(offset=update_id, timeout=10)
    for update in updates:
        next_update_id = update.update_id + 1

        # your bot can receive updates without messages
        # and not all messages contain text
        if update.message and update.message.text:
            # Reply to the message
            # logger.info("Found message %s!", update.message.text)
            await update.message.reply_text(update.message.text)
        return next_update_id
    return update_id


asyncio.run(main())
