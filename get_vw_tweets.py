import jsonpickle
import json
from twitter_client import get_twitter_client
from tweepy import TweepError

searchQuery = "#volkswagen OR $vlkay OR volkswagen"   # this is what we're searching for $vlkay,volkswagen
maxTweets = 100000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'vwtweets10122016.json' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = 786036699000344000

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
if __name__ == '__main__':
    client = get_twitter_client()
    
    print("Downloading max {0} tweets".format(maxTweets))
    with open(fName, 'w',encoding='utf-8') as f:
        #f.write('[')
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = client.search(q=searchQuery, count=tweetsPerQry)
                    else:
                        new_tweets = client.search(q=searchQuery, count=tweetsPerQry,
                                                since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = client.search(q=searchQuery, count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = client.search(q=searchQuery, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    f.write(jsonpickle.encode(tweet._json)+'\n')
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
    
            print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))