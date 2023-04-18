import openai

openai.api_key = "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"
model_engine = "davinci"

prompt = "Based on your quiz answers, we recommend that you make the following lifestyle changes:"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

recommendations = response.choices[0].text.strip()
print(recommendations)