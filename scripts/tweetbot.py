#!C:\python27 python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
msg = str(sys.argv[1])

print(msg)

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'Rp4xKV8DeO5TR6RyJlra39Tlg' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'sbDLefUi9NmVg2ViPY532sw0a886fiJDPZb79Uu3e7W4j2j3Lu' #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3223791542-czSD4V6I4W31kgYwSqpfAYAHQdEuyH4KCqDCVV7'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'lWvmZVmHUEvhPlZjTvN0324VHLriQlfEzDGCq92Lo7HhZ'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
api.update_status(status=msg)
