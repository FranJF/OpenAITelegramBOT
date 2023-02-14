import openai

openai.api_key = "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"
completion = openai.Completion.create(engine="text-davinci-003", prompt="", max_tokens=2048)
respuesta:str = completion.choices[0].text
print(respuesta)
