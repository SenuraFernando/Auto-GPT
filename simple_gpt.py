import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write an  essay about mobile phones"}])
print(completion.choices[0].message.content)