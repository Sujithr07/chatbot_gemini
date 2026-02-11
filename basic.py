from google import genai


client = genai.Client()
prompt = input("enter your prompt : ")

response = client.models.generate_content(
    model= 'gemini-2.5-flash',
    contents= prompt
)

print(response.text)