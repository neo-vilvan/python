import openai

openai.api_key = 

model = 'code-davinci-002'
prompt = input('Ask anything: ')


completion = openai.Completion.create(
    engine = model,
    prompt = prompt,
    max_tokens = 120,
    temperature = 0.0,
    n=1,
    stop=["###"],
    
)


response = completion.choices[0].text
print(response)