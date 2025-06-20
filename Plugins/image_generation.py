import os
import io
from dotenv import load_dotenv
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, 'Data', '.env')
load_dotenv(dotenv_path=ENV_PATH)
DREAMSTUDIO = os.getenv("DREAMSTUDIO_API")

def generate_image(prompt):
    stability_client = client.StabilityInference(
        key=DREAMSTUDIO,
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0", 
    )

    try:
        responses = stability_client.generate(
            prompt=prompt,
            seed=95456,
        )

        for response in responses:
            for artifact in response.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    print("Inappropriate image content was detected and filtered.")
                    return
                elif artifact.type == generation.ARTIFACT_IMAGE:
                    image = Image.open(io.BytesIO(artifact.binary))
                    image.show()
    except Exception as e:
        print(f"Error generating image: {e}")