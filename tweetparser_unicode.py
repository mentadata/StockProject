import json
import csv
import io

'''
creates a .csv file using a Twitter .json file
the fields have to be set manually
'''

csv_out = open('vwtweets10102016.csv', mode='w',encoding='utf-8') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = fields = ['id_str','created_at', 'text', 'screen_name', 'followers', 'friends', 'retweet_count', 'fav_count','hashtags','user_mention','lang','coordinates'] #field names
writer.writerow(fields) #writes field

def get_user_mention(tweet):
    entities = tweet.get('entities', {})
    user_mentions = entities.get('user_mentions', [])
    for um in user_mentions:
        return um['name']
        
def get_hashtags(tweet): 
  entities = tweet.get('entities', {}) 
  hashtags = entities.get('hashtags', []) 
  return [tag['text'].lower() for tag in hashtags]         
    
    

with open('vwtweets10102016.json', mode='r',encoding='utf-8') as f:
    for line in f:
        tweet = json.loads(line) # load it as Python dict
        writer.writerow([tweet.get('id_str'),
                     tweet.get('created_at'),
                     tweet.get('text'), #.encode('unicode_escape'), #unicode escape to fix emoji issue
                     tweet.get('user').get('screen_name'),
                     tweet.get('user').get('followers_count'),
                     tweet.get('user').get('friends_count'),
                     tweet.get('retweet_count'),
                     tweet.get('favorite_count'),
                     get_hashtags(tweet),
                     get_user_mention(tweet),
                     tweet.get('lang'),
                     tweet.get('coordinates'),
                     tweet.get('')])
    csv_out.close()
