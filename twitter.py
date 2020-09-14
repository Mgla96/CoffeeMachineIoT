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
            date = mention.created_at
            dif = current_utc-date
            time_delta=datetime.timedelta(days=1)
            if dif < time_delta:
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
        if mx[0]!="":
            print("people have chosen",mx[0], "as the coffee to make this morning. Starting Brew! Beep Boop")
            return (mx[0],mx[1])
        else:
            print("nobody voted :(")
            return (mx[0],mx[1])

if __name__=="__main__":
    twit=Twitter()
    coffee_choice,amount_votes=twit.getVote()
    print(coffee_choice,amount_votes)