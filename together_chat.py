from together import Together

# Initialize the Together client
client = Together()

# Create a chat completion request
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "user", "content": "Hello, how can I use DeepSeek?"}
    ],
    stream=True,
    tools=[]
)

# Stream and print the response
for token in response:
    if hasattr(token, 'choices'):
        print(token.choices[0].delta.content, end='', flush=True)
