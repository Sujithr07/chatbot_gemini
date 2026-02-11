from google import genai
from google.genai import types

client = genai.Client()
prompt = input("enter your prompt : ")

response = client.models.generate_content(
    model= 'gemini-2.5-flash',
    contents= prompt,
    config= types.GenerateContentConfig(
        system_instruction= "response must be in 25 words",
        temperature= 0.1
    )
)

print(response.text)