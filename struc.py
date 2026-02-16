from google import genai
from pydantic import BaseModel
import enum

class Grade(enum.Enum):
    A_plus= "a+"
    A="a"
    B="b"
    C="c"
    D="d"


class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]
    rating: Grade

client= genai.Client()

prompt= "give some popular indian recipes along with their ingredients"

response= client.models.generate_content(
    model= 'gemini-2.5-flash-lite',
    contents= prompt,
    config= {
        'response_mime_type':"application/json",
        'response_schema': list[Recipe]
    }

)

print(response.text)