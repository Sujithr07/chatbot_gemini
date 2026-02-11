from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()
prompt = input("enter your prompt : ")
image= Image.open("images/cat.jpg")

response = client.models.generate_content_stream(
    model= 'gemini-2.5-flash',
    contents= [image],
    config= types.GenerateContentConfig(
        system_instruction= "response must be in 50 words",
        temperature= 0.1
    )
)

# print(response.text)

for chunk in response:
    print(chunk.text,end="----- ")