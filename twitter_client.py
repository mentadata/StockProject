from tweepy import OAuthHandler
from tweepy import AppAuthHandler
from tweepy import API
import os
import sys


def get_twitter_auth():
    """   Setup Twitter Authentication    """
    try:
        """
        consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
        consumer_secret = os.environ["TWITTER_CONSUMER_KEY_SECRET"]
        access_token = os.environ["TWITTER_ACCESS_TOKEN"]
        access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
        """
        
        consumer_key = "fk8WvyFZcMMtEidPLgOgqiRTF"
        consumer_secret = "vW7xrCpfuieFeGdt0G0s4qqkcA6tnBvV9TPToSFJg7QhIaqAIG"
        access_token = "33776690-xOM1JXtB25KZsIbwWnw2D813cHJl4DdlvaqTfAPUf"
        access_token_secret = "xjmmWODbAvnjS8dbOZj1PRK01tpBAXSoL1hyCCKk9Vwbi"

        
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
        
    #auth = OAuthHandler(consumer_key,consumer_secret)                
    auth = AppAuthHandler(consumer_key,consumer_secret)
    #auth.set_access_token(access_token,access_token_secret)
    return auth
    
def get_twitter_client():
    print('setting client')
    auth = get_twitter_auth()
    client = API(auth,
                 wait_on_rate_limit = True, #Calls auto wait when rate limit is hit
                 wait_on_rate_limit_notify = True)
    return client
    
   
    
        
    
    




