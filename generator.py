import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


def get_hf_token():
    token = os.getenv("HF_TOKEN")

    if not token:
        raise ValueError(
            "HF_TOKEN is not configured. "
            "Please add your Hugging Face token to the .env file."
        )

    return token


def generate_image(prompt):
    client = InferenceClient(
        provider="auto",
        api_key=get_hf_token()
    )

    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    return image