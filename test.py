# import os
# import test_config
# api_key=os.environ['GEMINI_API_KEY']
# print(api_key)


import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access the variables
api_key = os.getenv("GEMINI_API_KEY")

# Print to verify (optional, do not print API keys in production)
print(api_key)  
