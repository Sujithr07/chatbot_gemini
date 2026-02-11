from google import genai
from google.genai import types


client= genai.Client()
chat= client.chats.create(model= 'gemini-2.5-flash-lite')

print("chat starts here.....   type 'end' to close")
userinput = input("User: ")

while userinput!='end':
    response= chat.send_message(userinput)
    print("Bot: ",response.text)
    userinput= input("User: ")


for message in chat.get_history():
    print(f"role - {message.role}")
    print(message.parts[0].text)
