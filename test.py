# tweeter posts a tweet

import os
from dotenv import load_dotenv
# import tweepy
import facebook  # Add Facebook SDK
import requests  # For making HTTP requests
#1st contribution comment
#2nd contribution comment


# Load environment variables from .env
load_dotenv()

# Access the variables
api_key = os.getenv("GEMINI_API_KEY")

# Print to verify (optional, do not print API keys in production)
print(f"API Key loaded: {'Yes' if api_key else 'No'}")

# Twitter API credentials
# consumer_key = os.getenv("TWITTER_API_KEY")
# consumer_secret = os.getenv("TWITTER_API_SECRET")
# access_token = os.getenv("TWITTER_ACCESS_TOKEN")
# access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Facebook API credentials
fb_app_id = os.getenv("FACEBOOK_APP_ID")
fb_app_secret = os.getenv("FACEBOOK_APP_SECRET")
fb_access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")  # If you already have a valid access token

def get_fb_access_token():
    """
    Get a Facebook App Access Token using App ID and App Secret.
    Note: This creates an App Access Token which cannot be used for posting to profiles or pages.
    For actual posting, you need a Page Access Token.
    """
    try:
        # Endpoint to get app access token
        token_url = f"https://graph.facebook.com/oauth/access_token?client_id={fb_app_id}&client_secret={fb_app_secret}&grant_type=client_credentials"
        
        # Make the request to get the token
        response = requests.get(token_url)
        data = response.json()
        
        if 'access_token' in data:
            print("App Access Token obtained successfully!")
            return data['access_token']
        else:
            print("Failed to get access token:", data)
            return None
    except Exception as e:
        print(f"Error getting Facebook access token: {str(e)}")
        return None

def post_facebook(content, page_id=None):
    """
    Post content to a Facebook Page using the provided access token.
    
    Parameters:
        content (str): The content to post
        page_id (str): ID of the page if posting to a specific page (None for default page)
    
    Note: You need a Page Access Token with proper permissions:
    - Page Access Token with BOTH 'pages_read_engagement' AND 'pages_manage_posts' permissions
    """
    try:
        # Try to use the stored access token
        token = fb_access_token
        
        # If no stored token, display error - app tokens won't work
        if not token:
            raise Exception("No valid Page Access Token available in your .env file")
            
        # Create Facebook Graph API object
        graph = facebook.GraphAPI(access_token=token)
        
        # Post the content to the page
        if page_id:
            # Post to a specific page using its ID
            graph.put_object(parent_object=page_id, connection_name='feed', message=content)
            print(f"Facebook post published successfully to page {page_id}!")
        else:
            # Post to the default page associated with the token
            graph.put_object(parent_object='me', connection_name='feed', message=content)
            print("Facebook post published to page successfully!")
        return True
    except Exception as e:
        error_message = str(e)
        print(f"Error posting to Facebook: {error_message}")
        
        print("\nTo resolve this error:")
        if "pages_read_engagement" in error_message or "pages_manage_posts" in error_message:
            print("You need a Page Access Token with:")
            print("  * BOTH 'pages_read_engagement' AND 'pages_manage_posts' permissions")
            print("  * You must be an admin of the page with sufficient permissions")
        else:
            print("For posting to a Facebook PAGE, you need:")
            print("  * Page Access Token with 'pages_read_engagement' and 'pages_manage_posts' permissions")
            print("  * You must be an admin of the page with sufficient permissions")
        
        print("\nHow to get a Page Access Token:")
        print("1. Go to https://developers.facebook.com/tools/explorer/")
        print("2. Select your app from the dropdown")
        print("3. Click 'Add Permissions' and add 'pages_read_engagement' and 'pages_manage_posts'")
        print("4. Generate Access Token (this gives you a User Access Token)")
        print("5. Change the request to '/me/accounts' and click Submit")
        print("6. Find your Page in the response and copy its access_token value")
        print("7. Add this token to your .env file as FACEBOOK_ACCESS_TOKEN")
        return False

# Example usage
if __name__ == "__main__":
    content = "Hello, this is a test post from my Python script! #Python"
    
    # Post to Facebook
    post_facebook(content)  # Post to your default page
    # post_facebook(content, '123456789')  # Post to a specific page with ID

# # def post_tweet(ntent):
# #     try:
# #         # Authticate with Twier
# #         auth = tweepy.OAuthHandler(consumer_key,onsumer_secret)
# #       auth.set_access_token(acce_token, access_token_secret)
        
# #         # Create API ject
# #         api =weepy.API(auth)
        
# #         # Pt the tweet
# #         api.update_stas(content)
# #         print("Tweet posted successfully!")
# #       return True
# #     except Exception as e:
# #         print(f"Error posti tweet: {str(e)}")
# #        eturn False

# # def post_facebook(content):#     """
# #     Post contento Facebook using the provided access ken.
# #     Note: You need a User Access Token  Page Access Token withroper permissions.
# #     App cess Token cannot be used for posting content to priles or pages.
# #     """     try:
# #         # Try tose the sted access token first
# #         token = fb_access_token
      
# #         # If no stored token, try to get an app access token (won't work for postg to profiles)
# #         if not token:
# #             token = get_fb_access_ton()
# #           prt("WARNING: App Access Tokens cannot be used for posng to profiles or pages.")
# #             pnt("You need a User Access Token or Page Access Token with appropriate permissions.")
        
# #       if not token:
# #           raise Exception("No valid access ken available")
            
# #         # Create Facebook Graph API object
# #         graph = facook.GraphAPI(access_token=token)
        
# #         # Post the content
# #         graph.put_object(parent_obje='me', connection_name=eed', message=content)
# #         print("Facebook post published successfully!
# #         return True
# #     except Exceptn as e:
# #         print(f"Error posting to Facebook: {str(e)}")         print("To post contt, you need:")
# #         print("1. A User Access Token (for posting to your profile)")#         print("2. A Page Access Token (for posting to page you manage)")
# #       print("3. Proper permsions (publish_actions, manage_pages, publish_pages)")         return False

# # # Example usage
# #f __name__ == "__main__":
# #     content = "Hello, this is a test post om my Python script! #Python"
# #     # post_tweet(content)  # Post to Twitte
# #     post_facebook(content)  # Post to Facebook  
