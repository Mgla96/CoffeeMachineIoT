import tweepy
import os 
from dotenv import load_dotenv
import time
import datetime
load_dotenv()

class Twitter():
    def __init__(self):
        auth=tweepy.OAuthHandler(os.environ.get("api_consumer_key"),os.environ.get("api_consumer_key_secret"))
        auth.set_access_token(os.environ.get("api_access_token"),os.environ.get("api_access_token_secret"))
        self.api=tweepy.API(auth)
    def getVote(self):
        mentions = self.api.mentions_timeline()
        #print(type(mentions[0]))
        #print(mentions[0].__dict__.keys())
        choice={}
        mx=["",0]
        current_utc = datetime.datetime.utcnow()
        for mention in mentions:
            #print(str(mention.id) + "-" + mention.text)
            date = mention.created_at
            dif = date-current_utc
            if dif < datetime.timedelta(0):
                text = mention.text.split()
                for word in text:
                    if word[0]=="#":
                        typ = word[1:]
                        if typ in choice:
                            choice[typ]+=1
                        else:
                            choice[typ]=1
                        if choice[typ]>mx[1]:
                            mx[1]=choice[typ]
                            mx[0]=typ
        print(mx)
        print("people have chosen",mx[0], "as the coffee to make this morning. Starting Brew! Beep Boop")
        return mx[0]
        '''
        for key in choice.keys():
            print(key)
        '''
