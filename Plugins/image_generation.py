import os
import io
from dotenv import load_dotenv
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

load_dotenv(dotenv_path = '..\\Data\\.env')
DREAMSTUDIO = os.getenv("DREAMSTUDIO_API")

def generate_image(prompt):
    client = client.stabilityInference(
        key = DREAMSTUDIO,
        verbose = True,
    )

    responses = client.generate(
        prompt = prompt,
        seed = 95456,
    )

    for response in responses:
        for artifact in response.artifacts:
            if artifact.finish_reason == generation.FILTER:
                print("Inappropriate image content was detected and filtered.")
                return
            elif artifact.type == generation.ARTIFACT_IMAGE:
                image = Image.open(io.BytesIO(artifact.binary()))
                image.show()