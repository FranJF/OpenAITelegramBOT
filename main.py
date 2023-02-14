import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY
completion = openai.Completion.create(engine="text-davinci-003", prompt="", max_tokens=2048)
respuesta:str = completion.choices[0].text
print(respuesta)
