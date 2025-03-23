from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

api_key = os.getenv("RAPID_API_KEY")  # Use os.getenv to avoid KeyError
