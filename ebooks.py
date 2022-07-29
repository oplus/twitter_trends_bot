import sys, tweepy

OAUTH_TOKEN = '##' #enter oauth token here
OAUTH_SECRET= '##' #enter oauth secret here
CONSUMER_KEY=  '##' #enter consumer key here
CONSUMER_SECRET= '##' #enter consumer secret here

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)

results = api.trends_place(23424802) #egypt trends

Fresults = []
counter = 1

def getdata():
    global counter
    for location in results:
        for trend in location["trends"][0:8]:
            Fresults.append(trend["name"])

    tweet = "\n".join(Fresults[0:8])

    if len(tweet) <= 140:
        return tweet
    else:
        while len(tweet) > 140:
            tweet = "\n".join(Fresults[0:8-counter])
            counter = counter + 1
            return tweet

#print getdata() + "\n" + str(len(getdata()))

try:
    api.update_status(status = getdata())
except: # I could use except tweepy.TweepError: (but used general expectation)
    pass
