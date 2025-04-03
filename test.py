# tweeter posts a tweet

import os
from dotenv import load_dotenv
# import tweepy
import facebook  # Add Facebook SDK

# Load environment variables from .env
load_dotenv()

# Access the variables
api_key = os.getenv("GEMINI_API_KEY")

# Print to verify (optional, do not print API keys in production)
print(api_key)

# Twitter API credentials
# consumer_key = os.getenv("TWITTER_API_KEY")
# consumer_secret = os.getenv("TWITTER_API_SECRET")
# access_token = os.getenv("TWITTER_ACCESS_TOKEN")
# access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


# Facebook API credentials
fb_access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")

# def post_tweet(content):
#     try:
#         # Authenticate with Twitter
#         auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#         auth.set_access_token(access_token, access_token_secret)
        
#         # Create API object
#         api = tweepy.API(auth)
        
#         # Post the tweet
#         api.update_status(content)
#         print("Tweet posted successfully!")
#         return True
#     except Exception as e:
#         print(f"Error posting tweet: {str(e)}")
#         return False

def post_facebook(content):
    try:
        # Create Facebook Graph API object
        graph = facebook.GraphAPI(access_token=fb_access_token)
        
        # Post the content
        graph.put_object(parent_object='me', connection_name='feed', message=content)
        print("Facebook post published successfully!")
        return True
    except Exception as e:
        print(f"Error posting to Facebook: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    content = "Hello, this is a test post from my Python script! #Python"
    # post_tweet(content)  # Post to Twitter
    post_facebook(content)  # Post to Facebook  
