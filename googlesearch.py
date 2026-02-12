from google import genai
from google.genai import types

client = genai.Client()
prompt = input("enter your prompt : ")

grounding_tool= types.Tool(
    google_search= types.GoogleSearch()
)

response = client.models.generate_content(
    model= 'gemini-2.5-flash',
    contents= prompt,
    config= types.GenerateContentConfig(
        tools=[grounding_tool]

    )
)

print(response.text)