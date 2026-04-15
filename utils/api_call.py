from google import genai
from dotenv import load_dotenv
from utils import casting_files
from gtts import gTTS
import os
import io


#LOADING THE ENVIRONMENT VARIABLE
load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

# INITIALIZING A CLIENT
Client = genai.Client(api_key = api_key)



def note_generator(images):
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
        response.text = "Something went wrong"
        
    return response.text


def audio_transcript(text):
    speech = gTTS(text , lang = 'en' , slow = False)

    audio_buffer = io.BytesIO()

    speech.write_to_fp(audio_buffer)

    return audio_buffer