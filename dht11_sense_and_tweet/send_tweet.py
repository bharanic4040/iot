#!/usr/bin/env python
import sys
from twython import Twython
import time


#change the below params of your twitter account
apiKey = 'U2pcVdFQhM01'
apiSecret = 'qayyayOX4z'
accessToken = '47pJIP4Ffff0v7IOgV'
accessTokenSecret = '2qs01'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
def send_tweet(temp,humid):
	status='temp:'+str(temp)+',humidity:'+str(humid)+',ts:'+str(time.time())
        api.update_status(status=status)
        print 'tweeted: '+status

