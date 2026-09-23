import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load .env when running locally
load_dotenv()


def get_hf_token():
    # First try environment variable
    token = os.getenv("HF_TOKEN")

    # If not found, try Streamlit Secrets
    if not token:
        try:
            token = st.secrets["HF_TOKEN"]
        except Exception:
            token = None

    if not token:
        raise ValueError(
            "HF_TOKEN is not configured. "
            "Please add HF_TOKEN in Streamlit Secrets."
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
