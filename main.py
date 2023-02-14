import openai

openai.api_key = "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"
completion = openai.Completion.create(engine="text-davinci-003", prompt="", max_tokens=2048)
respuesta:str = completion.choices[0].text
print(respuesta)
