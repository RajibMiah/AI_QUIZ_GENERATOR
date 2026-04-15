from google import genai
from dotenv import load_dotenv
from utils import casting_files
import os

#LOADING THE ENVIRONMENT VARIABLE
load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

# INITIALIZING A CLIENT
Client = genai.Client(api_key = api_key)



def note_genetor(images):
    try:
        pil_image = casting_files.generate_pil_image(images)
        prompt = """
                    Summarize the picture in note format at max 100 words
                    make sure to add necessary markdown to differentiate different section
                    """
        response  = Client.models.generate_content(
            model= "gemini-3-flash-preview",
            contents= [ pil_image , prompt]
        )
    except:
        response = "Something went wrong"
        
    return response.text