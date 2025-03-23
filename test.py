from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

api_key = os.getenv("put your api key here")  # Use os.getenv to avoid KeyError
