from google import genai
from google.genai import types
import httpx

client= genai.Client()

doc_url= "https://www.ijrti.org/papers/IJRTI2304061.pdf"
doc_data= httpx.get(doc_url).content
prompt="summarize the document"


pdf=types.Part.from_bytes(
    data= doc_data,
    mime_type="application/pdf"
)


response= client.models.generate_content(
    model= 'gemini-2.5-flash',
    contents= [pdf,prompt],
    config= types.GenerateContentConfig(
        system_instruction="answer in 200 words"
    )
)

print(response.text)