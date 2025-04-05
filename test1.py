# tweeter posts a tweet

import os
from dotenv import load_dotenv
import tweepy

# Load environment variables from .env
load_dotenv()

# Access the variables
api_key = os.getenv("GEMINI_API_KEY")

# Print to verify (optional, do not print API keys in production)
print(api_key)

# Twitter API credentials
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def post_tweet(content):
    try:
        # Authenticate with Twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        # Create API object
        api = tweepy.API(auth)
        
        # Post the tweet
        api.update_status(content)
        print("Tweet posted successfully!")
        return True
    except Exception as e:
        print(f"Error posting tweet: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    tweet_content = "Hello, this is "
    post_tweet(tweet_content)  



