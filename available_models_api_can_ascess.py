import google.generativeai as genai

genai.configure(api_key="AIzaSyDJpW9h_UIh7xYPOnki-2GAY0mLn6xGcWQ")

models = genai.list_models()
print("Available models:")
for m in models:
    print(m.name)
