import requests
from dotenv import load_dotenv
import os

load_dotenv()

BRIAN="nPczCjzI2devNBz1zQrb"
MODEL="eleven_multilingual_v2"
API_KEY=os.environ.get("11LABS_API")


TEXT="""

"""




url = f"https://api.elevenlabs.io/v1/text-to-speech/{BRIAN}"

payload = {
    "text": TEXT,
    "model_id": MODEL,
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5,
        #"style": 123, set by default to 0
        "use_speaker_boost": True
    }
    # "pronunciation_dictionary_locators": [
    #     {
    #         "pronunciation_dictionary_id": "<string>",
    #         "version_id": "<string>"
    #     }
    # ],
    # "seed": 123,
    # "previous_text": "<string>",
    # "next_text": "<string>",
    # "previous_request_ids": ["<string>"],
    # "next_request_ids": ["<string>"]
}

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": API_KEY
}

response = requests.request("POST", url, json=payload, headers=headers)

#print(response.text)


CHUNK_SIZE = 1024
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)