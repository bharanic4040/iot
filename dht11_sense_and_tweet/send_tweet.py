#!/usr/bin/env python
import sys
from twython import Twython
import time

apiKey = 'NXYzXgDTU2pcVy3gCgdFQhM01'
apiSecret = 'qayyayOlj4U0n040H6aQFJp4CT7CaTBbjGeJ0k7L0ZTJeO2X4z'
accessToken = '4734179119-nsQiNRmcdD53nF50FUkJwzYdPypJIP4F0v7IOgV'
accessTokenSecret = '2qs0PRG4HvFT53VdGKzC1V8Ts1PTQRKGGqy6jNPefV1m1'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
def send_tweet(temp,humid):
	status='temp:'+str(temp)+',humidity:'+str(humid)+',ts:'+str(time.time())
        api.update_status(status=status)
        print 'tweeted: '+status

