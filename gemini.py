from openai import OpenAI
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
    api_key= "AIzaSyDJpW9h_UIh7xYPOnki-2GAY0mLn6xGcWQ"
    )

completion = client.chat.completions.create(
    model="google/gemini-2.0-flash-lite-preview-02-05:free",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis which performs basic tasks like alexa and google cloud.Provide very short and concise answers, no more than 1-2 sentences."},
        {
            "role": "user",
            "content": "who is virat"
        }
    ]
)

print(completion.choices[0].message.content)