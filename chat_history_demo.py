# making the chat history manually with own logic

from google import genai
from google.genai import types


client= genai.Client()
print("chat starts here.....   type 'end' to close")

chat=[]
userinput = input("User: ")

while userinput!='end':
    chat.append("User: "+ userinput)
    response= client.models.generate_content(
        model= 'gemini-2.5-flash-lite',
        contents= userinput,
        config= types.GenerateContentConfig(
            system_instruction="answer in 1 line , within 50 words",
            temperature=0.1
        )
    )
    chat.append("Bot: "+ response.text)
    print("Bot: ",response.text)
    userinput= input("User: ")