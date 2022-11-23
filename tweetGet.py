import tweepy
import credentials
from pandas import DataFrame

api_key = credentials.API_KEY
api_key_secret = credentials.API_KEY_SECRET
bearer_token = credentials.BEARER_TOKEN
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Tweet a message
#tweetMessage = 'Hello World from Python Tweepy'
#api.update_status(tweetMessage)

userID = 'ManUtd'
tweets = api.user_timeline(screen_name=userID, 
                           count=200, 
                           include_rts = False,
                           exclude_replies = True,
                           tweet_mode = 'extended',
                           #max_id='1521591315317800965'
                           )

print(len(tweets))
for tweet in tweets:
     print(tweet.id_str), #1583086524823838723
     print(tweet.created_at), #2022-10-20 13:23:34+00:00
     print(tweet.favorite_count), #3149
     print(tweet.retweet_count),   #355
     print(tweet.full_text.encode("utf-8").decode("utf-8").replace('\n', ' ')) #A raucous, crackling atmosphere with

tweetCollector = []
tweetCollector.extend(tweets)
latestTweetId = tweets[-1].id

while True:
    tweets = api.user_timeline(screen_name=userID, 
                           count=200, 
                           include_rts = False,
                           exclude_replies = True,
                           tweet_mode = 'extended',
                           max_id = latestTweetId - 1,
                           )
    if len(tweets) == 0:
        print('Tweets = 0')
        break
    latestTweetId = tweets[-1].id
    tweetCollector.extend(tweets)
    print('Tweets downloaded so far:  {}'.format(len(tweetCollector)))
print('Exiting the while loop')

tweetsHelper = [['Manchester United',
                tweet.id_str, 
                tweet.created_at, 
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8").replace('\n', ' ')] for idx,tweet in enumerate(tweetCollector)]
df = DataFrame(tweetsHelper,columns=["club","id","createdAt","favorites","retweets","text"])
df.to_csv('Tweets_%s.csv' % userID,index=False)
print(df.head(5))