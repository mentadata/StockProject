import json
import csv

'''
creates a .csv file using a Twitter .json file
the fields have to be set manually
'''

csv_out = open('vwtweets10112016.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = fields = ['id_str','created_at', 'text', 'screen_name', 'followers', 'friends', 'rt', 'fav'] #field names
writer.writerow(fields) #writes field

with open('vwtweets10112016.json', 'r') as f:
    for line in f:
        print ("reading")
        tweet = json.loads(line) # load it as Python dict
        writer.writerow([tweet.get('id_str'),
                     tweet.get('created_at'),
                     tweet.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                     tweet.get('user').get('screen_name'),
                     tweet.get('user').get('followers_count'),
                     tweet.get('user').get('friends_count'),
                     tweet.get('retweet_count'),
                     tweet.get('favorite_count'),
                     tweet.get('')])
    csv_out.close()
